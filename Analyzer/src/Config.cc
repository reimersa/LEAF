#include <TString.h>
#include <TFile.h>
#include <TTreeIndex.h>
#include <iostream>
#include <sys/stat.h>

#include "LEAF/Analyzer/include/Config.h"
#include "LEAF/Analyzer/include/BaseTool.h"
#include "LEAF/Analyzer/include/useful_functions.h"

#include <libxml/parser.h>
#include <libxml/tree.h>
#include <libxml/xmlreader.h>

// #include <boost/filesystem.hpp>

using namespace std;

Config::Config(TString configfilename){
  if(m_is_init) throw runtime_error("Config object already initialized. Abort.");

  validateConfigFile(configfilename);
  xmlDoc *doc = xmlReadFile(configfilename, NULL, XML_PARSE_DTDATTR | XML_PARSE_NOENT | XML_PARSE_DTDVALID);
  xmlNode *root_element = xmlDocGetRootElement(doc);

  // Read general job information
  // ============================

  m_output_directory = getJobOutputpath(root_element);
  m_se_director = getJobSEDirector(root_element);
  m_postfix = getJobPostfix(root_element);
  m_target_lumi = getJobTargetlumi(root_element);
  m_analysis_tool = getJobAnalysisTool(root_element);
  m_nevt_max = getJobNEventsMax(root_element);
  if(m_nevt_max == 0) throw runtime_error("Apparently, 'NEventsMax = 0' has been specified in the config file. This is an invalid value, either set it to <0 (running on all events) or >0, then stopping after the specified number of events.");
  m_nevt_skip = getJobNEventsSkip(root_element);
  if(m_nevt_skip < 0) throw runtime_error("Apparently, 'NEventsSkip < 0' has been specified in the config file. This is an invalid value, set it to >= 0.");


  // Loop through InputDatasets and extract their information
  // ========================================================

  xmlNode *inputdatasets = findNodeByName(root_element, "InputDatasets");

  for (xmlNode* current_node = inputdatasets->children; current_node; current_node = current_node->next){
    if(current_node->type == XML_ELEMENT_NODE){
      dataset ds;
      ds.name     = getDatasetName(current_node);
      ds.type     = getDatasetType(current_node);
      ds.year     = getDatasetYear(current_node);
      ds.lumi     = getDatasetLumi(current_node);

      // loop over infiles of this dataset
      for (xmlNode* current_inputfile = current_node->children; current_inputfile; current_inputfile = current_inputfile->next){
        if(current_inputfile->type == XML_ELEMENT_NODE){
          ds.infilenames.emplace_back(getInputFileFileName(current_inputfile));
        }
      }
      m_datasets.emplace_back(ds);
    }
  }


  // Loop through additional variables and store to map
  // ==================================================

  xmlNode *addvars = findNodeByName(root_element, "AdditionalVariables");
  for (xmlNode* current_node = addvars->children; current_node; current_node = current_node->next){
    if(current_node->type == XML_ELEMENT_NODE){
      string name = getVariableName(current_node);
      string value = getVariableValue(current_node);
      TString message = "In Config: Additional variable with name ";
      message += name;
      message += " already used.";
      if(has(name)) throw runtime_error((string)message);
      m_additionalvariables[name] = value;
    }
  }


  // Loop through additional inputs and store to vector
  // ==================================================


  xmlNode *addcolls = findNodeByName(root_element, "AdditionalInputs");
  if(addcolls){
    vector<TString> existing_collections = {};
    for (xmlNode* current_node = addcolls->children; current_node; current_node = current_node->next){
      if(current_node->type == XML_ELEMENT_NODE){

        // here we are looking at one <AdditionalInput> at a time
        additional_input ai;
        vector<pair<TString, TString>> existing_datasets = {};




        // read in the collections that the above dataset should be used for
        for (xmlNode* ai_subnode = current_node->children; ai_subnode; ai_subnode = ai_subnode->next){
          if(ai_subnode->type == XML_ELEMENT_NODE){


            if(xmlStrEqual(ai_subnode->name, (xmlChar*)"AdditionalDataset")){

              // read in the dataset and check if a corresponding nominal dataset was defined in the xml file. Otherwise, this is ill-defined
              // xmlNode *dataset_node = findNodeByName(current_node, "AdditionalDataset");
              dataset ds;
              ds.name     = getDatasetName(ai_subnode);
              ds.year     = getDatasetYear(ai_subnode);

              // check if this dataset has a corresponding nominal dataset. Throw error if not
              bool is_defined_nominal_dataset = false;
              for(dataset nomds : m_datasets){
                if(nomds.name == ds.name && nomds.year == ds.year) is_defined_nominal_dataset = true;
              }
              string errormsg = "Additional dataset with name " + (string)ds.name + " and year " + (string)ds.year + " does not have a corresponding nominal dataset defined. Both the name and the year must be the same between nominal and additional samples.";
              if(!is_defined_nominal_dataset) throw runtime_error(errormsg);

              // check if this dataset exists already. Throw error if yes
              TString message = "In Config: In at least one <AdditionalInput>, an additional dataset with name ";
              message += ds.name;
              message += " and year ";
              message += ds.year;
              message += " already used.";
              for(pair<TString,TString> name_year_pair: existing_datasets ){
                if(ds.name == name_year_pair.first && ds.year == name_year_pair.second){
                  throw runtime_error(message);
                }
              }

              // loop over infiles of this dataset
              for (xmlNode* current_inputfile = ai_subnode->children; current_inputfile; current_inputfile = current_inputfile->next){
                if(current_inputfile->type == XML_ELEMENT_NODE){
                  ds.infilenames.emplace_back(getInputFileFileName(current_inputfile));
                }
              }

              // add dataset to list of datasets of this additional input
              ai.datasets.emplace_back(ds);
              existing_datasets.emplace_back(make_pair(ds.name, ds.year));

            }
            else if(xmlStrEqual(ai_subnode->name, (xmlChar*)"Collection")){

              collection coll;
              coll.classname = getCollectionClassname(ai_subnode);
              coll.branchname = getCollectionBranchname(ai_subnode);
              TString message = "In Config: Additional collection with name ";
              message += coll.branchname;
              message += " already used.";
              for(TString bn : existing_collections){
                if(bn == coll.branchname){
                  throw runtime_error((string)message);
                }
              }
              ai.collections.emplace_back(coll);
              existing_collections.emplace_back(coll.branchname);
            }
          }
        }

        cout << green << "--> Requesting " << ai.collections.size() << " additional collections from this additional input" << reset << endl;
        for(collection c: ai.collections){
          cout << green << "  --> Adding collection " << c.branchname << ", which contains objects of class " << c.classname << "." << reset << endl;
        }

        m_additionalinputs.emplace_back(ai);
      }
    }
  }

  xmlFreeDoc(doc);
  xmlCleanupParser();
  m_is_init = true;
}


void Config::process_datasets(){
  if(!m_is_init) throw runtime_error("Trying to process the datasets with an uninitialized Config instance. Abort.");

  // loop through samples
  while(idx() < n_datasets()){

    // Chain all samples of the same dataset into a TChain, for the nominal sample and the additional inputs (if any)
    event_chain.reset(new TChain("AnalysisTree"));
    m_additional_event_chains.clear();
    for(additional_input ai : m_additionalinputs){
      for(dataset ds : ai.datasets){
        if(ds.name == dataset_name() && ds.year == dataset_year()){
          shared_ptr<TChain> ch;
          ch.reset(new TChain("AnalysisTree"));
          m_additional_event_chains.emplace_back(ch);
        }
      }
    }
    cout << green << "--> Loading " << dataset_infilenames().size() << " input files for sample " << dataset_name() << "." << reset << endl;
    vector<TString> infilenames_lastparts = {};
    for(size_t i=0; i<dataset_infilenames().size(); i++){
      TString infilename_nominal = dataset_infilenames().at(i);
      event_chain->Add(infilename_nominal);
      TString tok;
      int from = 0;
      bool found_dotroot = false;
      while (infilename_nominal.Tokenize(tok, from, "/")) {
        if(found_dotroot){
          // this should never happen, because ".root" is always the last part of the filename, after the last "/".
          throw runtime_error("It seems like one of the additional input filenames has multiple occurrences of '.root'. This is currently not handeled properly and should be implemented. Please open a feature request on GitHub.");
        }
        if(tok.Contains(".root")){
          infilenames_lastparts.emplace_back(tok);
          found_dotroot = true;
        }
      }
    }

    nevt = event_chain->GetEntries();
    cout << green << "--> Loaded " << dataset_infilenames().size() << " files containing " << nevt << " events." << reset << endl;

    // load additional datasets, but only the rootfiles with the same number in the end (NTuple_22.root, for example)
    size_t idx_addeventchain = 0;
    vector<shared_ptr<TTreeIndex>> chain_indices = {};
    for(size_t i=0; i<m_additionalinputs.size(); i++){
      additional_input ai = m_additionalinputs.at(i);
      for(dataset ds : ai.datasets){
        if(ds.name == dataset_name() && ds.year == dataset_year()){
          for(TString infilename_add: ds.infilenames){
            bool use_this_infile = false;
            for(TString infilenames_lastpart: infilenames_lastparts){
              if(infilename_add.Contains(infilenames_lastpart)){
                use_this_infile = true;
              }
            }
            if(!use_this_infile) continue;
            m_additional_event_chains.at(idx_addeventchain)->Add(infilename_add);
          }
          shared_ptr<TTreeIndex> index;
          index.reset(new TTreeIndex(m_additional_event_chains.at(idx_addeventchain).get(), "lumiblock", "number"));
          m_additional_event_chains.at(idx_addeventchain)->SetTreeIndex(index.get());
          chain_indices.emplace_back(index);
          idx_addeventchain++;
        }
      }
    }
    cout << green << "--> Loaded " << m_additional_event_chains.size() << " additional event chains." << reset << endl;




    // make sure outdir exists
    TString mkdircommand = "LD_LIBRARY_PATH='' PYTHONPATH='' gfal-mkdir -p ";
    TString outfolder = output_directory();
    if(outfolder.Contains("/pnfs")){
      mkdircommand += se_director();
    }
    mkdircommand += outfolder;
    system((const char*)mkdircommand);

    // create output file and handle exception for /pnfs storage that is not immediately writeable
    TString filename_tmp = dataset_type() + "__" + dataset_name() + postfix() + "_tmp.root";
    TString outfilename_target = outfolder + "/" + filename_tmp;
    TString outfilename_tmp = outfilename_target;

    // this is PSI T3 specific, change in other environments!
    if(se_director() == "root://t3dcachedb03.psi.ch/" || se_director() == "root://storage01.lcg.cscs.ch/") {
      string tmpworkdirname = "/scratch/" + (string)getenv("USER") + "/tmp_workdir";
      string command = "mkdir -p " + (string)tmpworkdirname;
      system(command.c_str());
      outfilename_tmp = tmpworkdirname + "/" + filename_tmp;
    }

    outfile.reset(new TFile(outfilename_tmp, "RECREATE"));

    // create output tree
    outputtree = new TTree("AnalysisTree", "Events that passed the selection so far");

    // create instance of AnalysisTool and process this sample
    string toolname = analysis_tool();
    unique_ptr<BaseTool> analysis = ToolRegistry::build(toolname, *this);
    analysis->ProcessDataset(*this);

    // write output histograms and trees
    outfile->cd();
    analysis->WriteHistograms(*this);
    outputtree->OptimizeBaskets();
    outputtree->Write("", TObject::kOverwrite);
    outfile->Close();

    //rename tmp file
    TString outfilename_final = outfilename_target;
    outfilename_final.ReplaceAll("_tmp.root", ".root");

    TString command = "LD_LIBRARY_PATH='' PYTHONPATH='' gfal-copy -f " + outfilename_tmp + " ";
    if(outfolder.Contains("/pnfs")){
      command += se_director();
    }
    command += outfilename_final + " > /dev/null";

    system((const char*)command);
    command = "LD_LIBRARY_PATH='' PYTHONPATH='' gfal-rm " + outfilename_tmp + " > /dev/null";
    system((const char*)command);
    cout << green << "--> Wrote histograms and tree to file: " << outfilename_final << reset << endl << endl;

    increment_idx();
  }
}
