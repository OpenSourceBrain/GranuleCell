
# GranPassiveCond.channel.nml  missing as it's passive

# Note the -scaleDt=0.05. This is for Gran_KDr_98.channel.nml and Gran_H_98.channel.nml, which have very low time courses, and so require a smaller dt
pynml-channelanalysis -temperature 32 -html -md Gran_CaHVA_98.channel.nml  Gran_KA_98.channel.nml  Gran_KCa_98.channel.nml  Gran_NaF_98.channel.nml Gran_KDr_98.channel.nml Gran_H_98.channel.nml -scaleDt=0.05
