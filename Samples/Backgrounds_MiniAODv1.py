from Sample import *
from Storage import *
from collections import OrderedDict



# List of tuples ('samplename', sample itself) to be inserted orderly into an OrderedDict
backgroundlist = [
    ('TTToSemiLeptonic', Sample(
        type='MC',
        name='TTToSemiLeptonic',
        group=YearDependentContainer({'UL17': 'TT'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/TTToSemiLeptonic')}),
        xsecs=YearDependentContainer({'UL17': 364.31, '2018': 364.33}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/TTToSemiLeptonic.xml'}),
        nevents=YearDependentContainer({'UL17': 107110128013})
    )),

    ('TTTo2L2Nu', Sample(
        type='MC',
        name='TTTo2L2Nu',
        group=YearDependentContainer({'UL17': 'TT'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/TTTo2L2Nu')}),
        xsecs=YearDependentContainer({'UL17': 87.33, '2018': 87.33}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/TTTo2L2Nu.xml'}),
        nevents=YearDependentContainer({'UL17': 7707899548.41})
    )),

    ('TTToHadronic', Sample(
        type='MC',
        name='TTToHadronic',
        group=YearDependentContainer({'UL17': 'TT'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/TTToHadronic')}),
        xsecs=YearDependentContainer({'UL17': 380.11, '2018': 380.11}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/TTToHadronic.xml'}),
        nevents=YearDependentContainer({'UL17': 78077590542.8})
    )),

    ('WJetsToLNu_Inclusive', Sample(
        type='MC',
        name='WJetsToLNu_Inclusive',
        group=YearDependentContainer({'UL17': 'WJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/WJetsToLNu_Inclusive')}),
        xsecs=YearDependentContainer({'UL17': 53590.000000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/WJetsToLNu_Inclusive.xml'}),
        nevents=YearDependentContainer({'UL17': 1071670208.15})
    )),

    ('WJetsToLNu_HT70To100', Sample(
        type='MC',
        name='WJetsToLNu_HT70To100',
        group=YearDependentContainer({'UL17': 'WJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/WJetsToLNu_HT70To100')}),
        xsecs=YearDependentContainer({'UL17': 1273.000000 * 1.21}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/WJetsToLNu_HT70To100.xml'}),
        nevents=YearDependentContainer({'UL17': 44307585.0})
    )),

    ('WJetsToLNu_HT100To200', Sample(
        type='MC',
        name='WJetsToLNu_HT100To200',
        group=YearDependentContainer({'UL17': 'WJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/WJetsToLNu_HT100To200')}),
        xsecs=YearDependentContainer({'UL17': 1255.000000 * 1.21}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/WJetsToLNu_HT100To200.xml'}),
        nevents=YearDependentContainer({'UL17': 47314843.0})
    )),

    ('WJetsToLNu_HT200To400', Sample(
        type='MC',
        name='WJetsToLNu_HT200To400',
        group=YearDependentContainer({'UL17': 'WJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/WJetsToLNu_HT200To400')}),
        xsecs=YearDependentContainer({'UL17': 336.400000 * 1.21}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/WJetsToLNu_HT200To400.xml'}),
        nevents=YearDependentContainer({'UL17': 40343957.0})
    )),

    ('WJetsToLNu_HT400To600', Sample(
        type='MC',
        name='WJetsToLNu_HT400To600',
        group=YearDependentContainer({'UL17': 'WJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/WJetsToLNu_HT400To600')}),
        xsecs=YearDependentContainer({'UL17': 45.250000 * 1.21}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/WJetsToLNu_HT400To600.xml'}),
        nevents=YearDependentContainer({'UL17': 5281776.0})
    )),

    ('WJetsToLNu_HT600To800', Sample(
        type='MC',
        name='WJetsToLNu_HT600To800',
        group=YearDependentContainer({'UL17': 'WJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/WJetsToLNu_HT600To800')}),
        xsecs=YearDependentContainer({'UL17': 10.990000 * 1.21}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/WJetsToLNu_HT600To800.xml'}),
        nevents=YearDependentContainer({'UL17': 5457844.0})
    )),

    ('WJetsToLNu_HT800To1200', Sample(
        type='MC',
        name='WJetsToLNu_HT800To1200',
        group=YearDependentContainer({'UL17': 'WJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/WJetsToLNu_HT800To1200')}),
        xsecs=YearDependentContainer({'UL17': 4.924000 * 1.21}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/WJetsToLNu_HT800To1200.xml'}),
        nevents=YearDependentContainer({'UL17': 5227462.0})
    )),

    ('WJetsToLNu_HT1200To2500', Sample(
        type='MC',
        name='WJetsToLNu_HT1200To2500',
        group=YearDependentContainer({'UL17': 'WJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/WJetsToLNu_HT1200To2500')}),
        xsecs=YearDependentContainer({'UL17': 1.157000 * 1.21}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/WJetsToLNu_HT1200To2500.xml'}),
        nevents=YearDependentContainer({'UL17': 4932173.0})
    )),

    ('DYJetsToLL_M10To50_Inclusive', Sample(
        type='MC',
        name='DYJetsToLL_M10To50_Inclusive',
        group=YearDependentContainer({'UL17': 'DYJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/DYJetsToLL_M10To50_Inclusive')}),
        xsecs=YearDependentContainer({'UL17': 15900.000000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/DYJetsToLL_M10To50_Inclusive.xml'}),
        nevents=YearDependentContainer({'UL17': 69819307.0})
    )),

    ('DYJetsToLL_M50_Inclusive', Sample(
        type='MC',
        name='DYJetsToLL_M50_Inclusive',
        group=YearDependentContainer({'UL17': 'DYJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/DYJetsToLL_M50_Inclusive')}),
        xsecs=YearDependentContainer({'UL17': 5352.000000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/DYJetsToLL_M50_Inclusive.xml'}),
        nevents=YearDependentContainer({'UL17': 1819671163.1})
    )),

    ('DYJetsToLL_M50_HT70To100', Sample(
        type='MC',
        name='DYJetsToLL_M50_HT70To100',
        group=YearDependentContainer({'UL17': 'DYJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/DYJetsToLL_M50_HT70To100')}),
        xsecs=YearDependentContainer({'UL17': 139.500000 * 1.23}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/DYJetsToLL_M50_HT70To100.xml'}),
        nevents=YearDependentContainer({'UL17': 12893327.0})
    )),

    ('DYJetsToLL_M50_HT100To200', Sample(
        type='MC',
        name='DYJetsToLL_M50_HT100To200',
        group=YearDependentContainer({'UL17': 'DYJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/DYJetsToLL_M50_HT100To200')}),
        xsecs=YearDependentContainer({'UL17': 140.400000 * 1.23}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/DYJetsToLL_M50_HT100To200.xml'}),
        nevents=YearDependentContainer({'UL17': 20003974.0})
    )),

    ('DYJetsToLL_M50_HT200To400', Sample(
        type='MC',
        name='DYJetsToLL_M50_HT200To400',
        group=YearDependentContainer({'UL17': 'DYJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/DYJetsToLL_M50_HT200To400')}),
        xsecs=YearDependentContainer({'UL17': 38.360000 * 1.23}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/DYJetsToLL_M50_HT200To400.xml'}),
        nevents=YearDependentContainer({'UL17': 11081825.0})
    )),

    ('DYJetsToLL_M50_HT400To600', Sample(
        type='MC',
        name='DYJetsToLL_M50_HT400To600',
        group=YearDependentContainer({'UL17': 'DYJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/DYJetsToLL_M50_HT400To600')}),
        xsecs=YearDependentContainer({'UL17': 5.222000 * 1.23}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/DYJetsToLL_M50_HT400To600.xml'}),
        nevents=YearDependentContainer({'UL17': 6020252.0})
    )),

    ('DYJetsToLL_M50_HT600To800', Sample(
        type='MC',
        name='DYJetsToLL_M50_HT600To800',
        group=YearDependentContainer({'UL17': 'DYJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/DYJetsToLL_M50_HT600To800')}),
        xsecs=YearDependentContainer({'UL17': 1.264000 * 1.23}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/DYJetsToLL_M50_HT600To800.xml'}),
        nevents=YearDependentContainer({'UL17': 5735614.0})
    )),

    ('DYJetsToLL_M50_HT800To1200', Sample(
        type='MC',
        name='DYJetsToLL_M50_HT800To1200',
        group=YearDependentContainer({'UL17': 'DYJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/DYJetsToLL_M50_HT800To1200')}),
        xsecs=YearDependentContainer({'UL17': 0.568500 * 1.23}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/DYJetsToLL_M50_HT800To1200.xml'}),
        nevents=YearDependentContainer({'UL17': 4923581.0})
    )),

    ('DYJetsToLL_M50_HT1200To2500', Sample(
        type='MC',
        name='DYJetsToLL_M50_HT1200To2500',
        group=YearDependentContainer({'UL17': 'DYJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/DYJetsToLL_M50_HT1200To2500')}),
        xsecs=YearDependentContainer({'UL17': 0.133000 * 1.23}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/DYJetsToLL_M50_HT1200To2500.xml'}),
        nevents=YearDependentContainer({'UL17': 4674099.0})
    )),

    ('DYJetsToLL_M50_HT2500ToInf', Sample(
        type='MC',
        name='DYJetsToLL_M50_HT2500ToInf',
        group=YearDependentContainer({'UL17': 'DYJets'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/DYJetsToLL_M50_HT2500ToInf')}),
        xsecs=YearDependentContainer({'UL17': 0.002981 * 1.23}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/DYJetsToLL_M50_HT2500ToInf.xml'}),
        nevents=YearDependentContainer({'UL17': 1428101.0})
    )),

    ('ST_tch_ele', Sample(
        type='MC',
        name='ST_tch_ele',
        group=YearDependentContainer({'UL17': 'ST'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/ST_tch_ele')}),
        xsecs=YearDependentContainer({'UL17': 24.780000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/ST_tch_ele.xml'}),
        nevents=YearDependentContainer({'UL17': 1177725.0})
    )),

    ('ST_tch_mu', Sample(
        type='MC',
        name='ST_tch_mu',
        group=YearDependentContainer({'UL17': 'ST'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/ST_tch_mu')}),
        xsecs=YearDependentContainer({'UL17': 24.770000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/ST_tch_mu.xml'}),
        nevents=YearDependentContainer({'UL17': 1117652.0})
    )),

    ('ST_tch_tau', Sample(
        type='MC',
        name='ST_tch_tau',
        group=YearDependentContainer({'UL17': 'ST'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/ST_tch_tau')}),
        xsecs=YearDependentContainer({'UL17': 24.760000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/ST_tch_tau.xml'}),
        nevents=YearDependentContainer({'UL17': 1149875.0})
    )),

    ('ST_sch', Sample(
        type='MC',
        name='ST_sch',
        group=YearDependentContainer({'UL17': 'ST'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/ST_sch')}),
        xsecs=YearDependentContainer({'UL17': 3.36}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/ST_sch.xml'}),
        nevents=YearDependentContainer({'UL17': 26048549.2057})
    )),

    ('ST_tW_top', Sample(
        type='MC',
        name='ST_tW_top',
        group=YearDependentContainer({'UL17': 'ST'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/ST_tW_top')}),
        xsecs=YearDependentContainer({'2016': 71.7*0.5*0.546, 'UL17': 71.7*0.5*0.546, '2018': 71.7*0.5*0.546}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/ST_tW_top.xml'}),
        nevents=YearDependentContainer({'UL17': 275070817.636})
    )),

    ('ST_tW_antitop', Sample(
        type='MC',
        name='ST_tW_antitop',
        group=YearDependentContainer({'UL17': 'ST'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/ST_tW_antitop')}),
        xsecs=YearDependentContainer({'2016': 71.7*0.5*0.546, 'UL17': 71.7*0.5*0.546, '2018': 71.7*0.5*0.546}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/ST_tW_antitop.xml'}),
        nevents=YearDependentContainer({'UL17': 270345271.852})
    )),

    ('WW_2L2Nu', Sample(
        type='MC',
        name='WW_2L2Nu',
        group=YearDependentContainer({'UL17': 'VV'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/WW_2L2Nu')}),
        xsecs=YearDependentContainer({'UL17': 11.090000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/WW_2L2Nu.xml'}),
        nevents=YearDependentContainer({'UL17': 76582077.7076})
    )),

    ('WZ_3LNu', Sample(
        type='MC',
        name='WZ_3LNu',
        group=YearDependentContainer({'UL17': 'VV'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/WZTo3LNu_mllmin01_NNPDF31_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/WZ_3LNu')}),
        xsecs=YearDependentContainer({'UL17': 4.664000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/WZ_3LNu.xml'}),
        nevents=YearDependentContainer({'UL17': 289652756.74})
    )),

    ('ZZ_2L2Nu', Sample(
        type='MC',
        name='ZZ_2L2Nu',
        group=YearDependentContainer({'UL17': 'VV'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/ZZ_2L2Nu')}),
        xsecs=YearDependentContainer({'UL17': 0.973800}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/ZZ_2L2Nu.xml'}),
        nevents=YearDependentContainer({'UL17': 39451110.7339})
    )),

    ('ZZ_4L', Sample(
        type='MC',
        name='ZZ_4L',
        group=YearDependentContainer({'UL17': 'VV'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/ZZ_4L')}),
        xsecs=YearDependentContainer({'UL17': 13.810000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/ZZ_4L.xml'}),
        nevents=YearDependentContainer({'UL17': 575838493.735})
    )),

    ('QCD_Pt_15to30', Sample(
        type='MC',
        name='QCD_Pt_15to30',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_15to30')}),
        xsecs=YearDependentContainer({'UL17': 1245000000.000000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_15to30.xml'}),
        nevents=YearDependentContainer({'UL17': 19939903.0})
    )),

    ('QCD_Pt_30to50', Sample(
        type='MC',
        name='QCD_Pt_30to50',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_30to50')}),
        xsecs=YearDependentContainer({'UL17': 105800000.000000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_30to50.xml'}),
        nevents=YearDependentContainer({'UL17': 19685000.0})
    )),

    ('QCD_Pt_50to80', Sample(
        type='MC',
        name='QCD_Pt_50to80',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_50to80')}),
        xsecs=YearDependentContainer({'UL17': 15560000.000000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_50to80.xml'}),
        nevents=YearDependentContainer({'UL17': 20000000.0})
    )),

    ('QCD_Pt_80to120', Sample(
        type='MC',
        name='QCD_Pt_80to120',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_80to120')}),
        xsecs=YearDependentContainer({'UL17': 2319000.000000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_80to120.xml'}),
        nevents=YearDependentContainer({'UL17': 29994396.7735})
    )),

    ('QCD_Pt_120to170', Sample(
        type='MC',
        name='QCD_Pt_120to170',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_120to170')}),
        xsecs=YearDependentContainer({'UL17': 403500.000000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_120to170.xml'}),
        nevents=YearDependentContainer({'UL17': 29544358.6683})
    )),

    ('QCD_Pt_170to300', Sample(
        type='MC',
        name='QCD_Pt_170to300',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_170to300')}),
        xsecs=YearDependentContainer({'UL17': 102600.000000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_170to300.xml'}),
        nevents=YearDependentContainer({'UL17': 29663925.0})
    )),

    ('QCD_Pt_300to470', Sample(
        type='MC',
        name='QCD_Pt_300to470',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_300to470')}),
        xsecs=YearDependentContainer({'UL17': 6760.000000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_300to470.xml'}),
        nevents=YearDependentContainer({'UL17': 56716009.0493})
    )),

    ('QCD_Pt_470to600', Sample(
        type='MC',
        name='QCD_Pt_470to600',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_470to600')}),
        xsecs=YearDependentContainer({'UL17': 545.900000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_470to600.xml'}),
        nevents=YearDependentContainer({'UL17': 52760173.1235})
    )),

    ('QCD_Pt_600to800', Sample(
        type='MC',
        name='QCD_Pt_600to800',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_600to800')}),
        xsecs=YearDependentContainer({'UL17': 154.700000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_600to800.xml'}),
        nevents=YearDependentContainer({'UL17': 67850001.6094})
    )),

    ('QCD_Pt_800to1000', Sample(
        type='MC',
        name='QCD_Pt_800to1000',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_800to1000')}),
        xsecs=YearDependentContainer({'UL17': 25.950000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_800to1000.xml'}),
        nevents=YearDependentContainer({'UL17': 37527285.0})
    )),

    ('QCD_Pt_1000to1400', Sample(
        type='MC',
        name='QCD_Pt_1000to1400',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_1000to1400')}),
        xsecs=YearDependentContainer({'UL17': 7.398000}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_1000to1400.xml'}),
        nevents=YearDependentContainer({'UL17': 19905692.0})
    )),

    ('QCD_Pt_1400to1800', Sample(
        type='MC',
        name='QCD_Pt_1400to1800',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_1400to1800')}),
        xsecs=YearDependentContainer({'UL17': 0.642300}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_1400to1800.xml'}),
        nevents=YearDependentContainer({'UL17': 10994000.0})
    )),

    ('QCD_Pt_1800to2400', Sample(
        type='MC',
        name='QCD_Pt_1800to2400',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_1800to2400')}),
        xsecs=YearDependentContainer({'UL17': 0.086710}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_1800to2400.xml'}),
        nevents=YearDependentContainer({'UL17': 5491000.0})
    )),

    ('QCD_Pt_2400to3200', Sample(
        type='MC',
        name='QCD_Pt_2400to3200',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_2400to3200')}),
        xsecs=YearDependentContainer({'UL17': 0.005193}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_2400to3200.xml'}),
        nevents=YearDependentContainer({'UL17': 2997000.0})
    )),

    ('QCD_Pt_3200toInf', Sample(
        type='MC',
        name='QCD_Pt_3200toInf',
        group=YearDependentContainer({'UL17': 'QCD_Had'}),
        minipaths=YearDependentContainer({'UL17': Storage_DAS('/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM')}),
        tuplepaths=YearDependentContainer({'UL17': Storage_T3PSI('/store/user/areimers/UL17/Summer20/Tuples_v00_MINIAOD/QCD_Pt_3200toInf')}),
        xsecs=YearDependentContainer({'UL17': 0.000134}),
        xmlfiles=YearDependentContainer({'UL17': 'datasets/UL17/Summer20/MINIAOD/QCD_Pt_3200toInf.xml'}),
        nevents=YearDependentContainer({'UL17': 1000000.0})
    )),
]
    # }