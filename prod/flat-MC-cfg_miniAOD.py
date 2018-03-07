import FWCore.ParameterSet.Config as cms 

process = cms.Process('jetToolbox')

process.load('PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

## ----------------- Global Tag ------------------
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.GlobalTag.globaltag = '80X_dataRun2_Prompt_ICHEP16JEC_v0' 
#process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_miniAODv2_v0'


#--------------------- Report and output ---------------------------

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-100))

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000


process.TFileService=cms.Service("TFileService",
                                 fileName=cms.string('THISROOTFILE.root'),
                                 #fileName=cms.string("test.root"),
                                 closeFileFast = cms.untracked.bool(True)
                                 )

## --- suppress long output ---> wantSummary = cms.untracked.bool(False) 

process.options = cms.untracked.PSet(
        allowUnscheduled = cms.untracked.bool(True),
        wantSummary = cms.untracked.bool(False),
)

############## output  edm format ###############
process.out = cms.OutputModule('PoolOutputModule',                                                                                                                  
                               fileName = cms.untracked.string('jettoolbox.root'),                                                                              
                               outputCommands = cms.untracked.vstring([
                                                                      'keep *_slimmedJets_*_*',                                                                  
                                                                      'keep *_slimmedJetsAK8_*_*',                                                                  
                                                                       ])                                                                                           
                               )


# ----------------------- Jet Tool Box  -----------------
# ----- giulia test: do not recluster ak4 and ca8 jets to save time --------

process.chs = cms.EDFilter('CandPtrSelector', src = cms.InputTag('packedPFCandidates'), cut = cms.string('fromPV'))

from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
process.slimmedGenJetsAK8 = ak4GenJets.clone(src = 'packedGenParticles', rParam = 0.8)


#-------------------------------------------------------
# Gen Particles Pruner
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.prunedGenParticlesDijet = cms.EDProducer('GenParticlePruner',
    src = cms.InputTag("prunedGenParticles"),
    select = cms.vstring(
    "drop  *  ", # by default
    "keep ( status = 3 || (status>=21 && status<=29) )", # keep hard process particles
    )
)


#------------- Recluster Gen Jets to access the constituents -------
#already in toolbox, just add keep statements

process.out.outputCommands.append("keep *_slimmedGenJets_*_*")
process.out.outputCommands.append("keep *_slimmedGenJetsAK8_*_*")

##-------------------- Define the source  ----------------------------



process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('file:QstarToJJ_M_4000_TuneCUETP8M1_13TeV_pythia8__MINIAODSIM__Asympt50ns_MCRUN2_74_V9A-v1__70000__AA35D1E7-FEFE-E411-B1C5-0025905B858A.root')    
    #fileNames = cms.untracked.vstring('/store/mc/RunIISpring15DR74/QstarToJJ_M_1000_TuneCUETP8M1_13TeV_pythia8/AODSIM/Asympt50ns_MCRUN2_74_V9A-v1/50000/00F85752-BCFB-E411-A29A-000F5327349C.root')
    #fileNames = cms.untracked.vstring('root://xrootd.unl.edu//store/mc/RunIISpring15DR74/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/0E4CEBFE-ECFB-E411-9F0C-842B2B29273C.root')
    fileNames = cms.untracked.vstring(
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/0A98E175-AB99-E711-8619-0CC47A7C3628.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/262B689A-269C-E711-9E23-02163E01A33D.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/4CEB149D-2599-E711-B9EE-0CC47A13CC7E.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/6C97DF0E-E099-E711-B490-44A842CF05F3.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/7C8B6CE3-4E98-E711-B664-24BE05CE2D41.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/8E05F2EA-3E99-E711-B3C7-A4BF0112BC5E.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/9674C3D7-EF99-E711-B994-0025905C96EA.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/A4902362-EF99-E711-AEAA-24BE05C60641.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/B6A3043D-2899-E711-8CDF-4C79BA181343.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/C41A6BF7-EF99-E711-883F-0025905A60F8.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/EE1B0E3D-C899-E711-80EC-001E67A42161.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/F488AA65-EF99-E711-A072-1866DAEEB344.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/F81AFAF7-5999-E711-B651-7CD30ACE18E8.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/50000/FE9AC807-F099-E711-86D4-0025907DE266.root',
'/store/mc/RunIISummer17MiniAOD/RSGravitonToQuarkQuark_kMpl01_M_4000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/92X_upgrade2017_realistic_v10-v1/510000/C2D3182A-1F9C-E711-A5DD-02163E011B4D.root'
)
    )




##-------------------- User analyzer  --------------------------------

#Residue from deleted reco and AOD sequences
calo_collection=''
cluster_collection=''
pfcalo_collection=''
   

process.dijets     = cms.EDAnalyzer('DijetTreeProducer',
  
  # There's no avoiding this in Consumes era
  isData          = cms.bool(False),
  
  jetsAK4             = cms.InputTag('slimmedJets'), 
  jetsAK8             = cms.InputTag('slimmedJetsAK8'),     
  rho              = cms.InputTag('fixedGridRhoFastjetAll'),
  met              = cms.InputTag('slimmedMETs'),
  vtx              = cms.InputTag('offlineSlimmedPrimaryVertices'),
  ptMinAK4         = cms.double(10),
  ptMinAK8         = cms.double(10),

  ## MC ########################################
  pu               = cms.untracked.InputTag('slimmedAddPileupInfo'),
  ptHat            = cms.untracked.InputTag('generator'),
  genParticles     = cms.InputTag('prunedGenParticlesDijet'),
  genJetsAK4             = cms.InputTag('slimmedGenJets'), 
  genJetsAK8             = cms.InputTag('slimmedGenJetsAK8'),     


  ## trigger ###################################
  triggerAlias     = cms.vstring('PFHT900','PFHT650','PFHT600','PFHT350'
                                 ,'PFHT650MJJ950','PFHT650MJJ900'
                                 ,'PFJET500','PFJET450','PFJET200'),
  triggerSelection = cms.vstring(
     'HLT_PFHT900_v*',
     'HLT_PFHT650_v*',
     'HLT_PFHT600_v*',
     'HLT_PFHT350_v*',
     'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v*',
     'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v*',
     'HLT_PFJet500_v*',
     'HLT_PFJet450_v*',
     'HLT_PFJet200_v*',
     
  ),
  triggerConfiguration = cms.PSet(
    hltResults            = cms.InputTag('TriggerResults','','HLT'),
    l1tResults            = cms.InputTag(''),
    daqPartitions         = cms.uint32(1),
    l1tIgnoreMask         = cms.bool(False),
    l1techIgnorePrescales = cms.bool(False),
    l1tIgnoreMaskAndPrescale= cms.bool(False),
    throw                 = cms.bool(False)
  ),

  ## Noise Filters ###################################
  noiseFilterSelection_BadPFMuonFilter = cms.string('Flag_BadPFMuonFilter'),
  noiseFilterSelection_BadChargedCandidateFilter = cms.string('Flag_BadChargedCandidateFilter'),
  noiseFilterSelection_HBHENoiseIsoFilter = cms.string('Flag_HBHENoiseIsoFilter'),
  noiseFilterSelection_HBHENoiseFilter = cms.string('Flag_HBHENoiseFilter'),
  noiseFilterSelection_CSCTightHaloFilter = cms.string('Flag_CSCTightHaloFilter'),
  noiseFilterSelection_hcalLaserEventFilter = cms.string('Flag_hcalLaserEventFilter'),
  noiseFilterSelection_EcalDeadCellTriggerPrimitiveFilter = cms.string('Flag_EcalDeadCellTriggerPrimitiveFilter'),
  noiseFilterSelection_goodVertices = cms.string('Flag_goodVertices'),
  noiseFilterSelection_trackingFailureFilter = cms.string('Flag_trackingFailureFilter'),
  noiseFilterSelection_eeBadScFilter = cms.string('Flag_eeBadScFilter'),
  noiseFilterSelection_ecalLaserCorrFilter = cms.string('Flag_ecalLaserCorrFilter'),
  noiseFilterSelection_trkPOGFilters = cms.string('Flag_trkPOGFilters'),
  noiseFilterSelection_globalSuperTightHalo2016Filter = cms.string('Flag_globalSuperTightHalo2016Filter'),
  # and the sub-filters
  noiseFilterSelection_trkPOG_manystripclus53X = cms.string('Flag_trkPOG_manystripclus53X'),
  noiseFilterSelection_trkPOG_toomanystripclus53X = cms.string('Flag_trkPOG_toomanystripclus53X'),
  noiseFilterSelection_trkPOG_logErrorTooManyClusters = cms.string('Flag_trkPOG_logErrorTooManyClusters'),

  noiseFilterConfiguration = cms.PSet(
    hltResults            = cms.InputTag('TriggerResults','','PAT'),
    l1tResults            = cms.InputTag(''),
    daqPartitions         = cms.uint32(1),
    l1tIgnoreMask         = cms.bool(False),
    l1techIgnorePrescales = cms.bool(False),
    l1tIgnoreMaskAndPrescale= cms.bool(False),
    throw                 = cms.bool(False)
  ),


  ## JECs ################
  redoJECs  = cms.bool(True),

  ## Version Summer15_25nsV3
  L1corrAK4_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_DATA/Spring16_25nsV6_DATA_L1FastJet_AK4PFchs.txt'),
  L2corrAK4_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_DATA/Spring16_25nsV6_DATA_L2Relative_AK4PFchs.txt'),
  L3corrAK4_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_DATA/Spring16_25nsV6_DATA_L3Absolute_AK4PFchs.txt'),
  ResCorrAK4_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_DATA/Spring16_25nsV6_DATA_L2L3Residual_AK4PFchs.txt'),
  L1corrAK8_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_DATA/Spring16_25nsV6_DATA_L1FastJet_AK8PFchs.txt'),
  L2corrAK8_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_DATA/Spring16_25nsV6_DATA_L2Relative_AK8PFchs.txt'),
  L3corrAK8_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_DATA/Spring16_25nsV6_DATA_L3Absolute_AK8PFchs.txt'),
  ResCorrAK8_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_DATA/Spring16_25nsV6_DATA_L2L3Residual_AK4PFchs.txt'),
  L1corrAK4_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_MC/Spring16_25nsV6_MC_L1FastJet_AK4PFchs.txt'),
  L2corrAK4_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_MC/Spring16_25nsV6_MC_L2Relative_AK4PFchs.txt'),
  L3corrAK4_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_MC/Spring16_25nsV6_MC_L3Absolute_AK4PFchs.txt'),
  L1corrAK8_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_MC/Spring16_25nsV6_MC_L1FastJet_AK8PFchs.txt'),
  L2corrAK8_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_MC/Spring16_25nsV6_MC_L2Relative_AK8PFchs.txt'),
  L3corrAK8_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Spring16_25nsV6_MC/Spring16_25nsV6_MC_L3Absolute_AK8PFchs.txt')
)


# ------------------ path --------------------------

process.p = cms.Path()

process.p +=                     process.prunedGenParticlesDijet
process.p +=                     process.chs 
process.p +=                     process.slimmedGenJetsAK8                      
process.p +=                     process.dijets 
