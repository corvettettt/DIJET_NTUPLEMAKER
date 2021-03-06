from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = '/uscms_data/d3/zwang2/CMSSW_9_4_0/src/CMSDIJET/DijetRootTreeMaker/crab_jobs/'
config.General.requestName = 'QCD_1000-1500'
config.JobType.psetName = '/uscms_data/d3/zwang2/CMSSW_9_4_0/src/CMSDIJET/DijetRootTreeMaker/prod/flat-MC-cfg_miniAOD.py'
config.JobType.pluginName = 'Analysis'
config.Data.inputDataset = 'global'
config.Data.inputDataset = '/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v2/MINIAODSIM' 
config.Data.unitsPerJob = 1 #without '' since it must be an int
config.Data.splitting = 'FileBased'
config.Data.publication = False
config.Data.outputDatasetTag = 'analysis'
config.Data.outLFNDirBase = '/store/user/%s/GravitonToQuarkQuark/' % (getUsernameFromSiteDB())
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
config.Site.blacklist = []
config.Site.storageSite = 'T3_US_FNALLPC'
