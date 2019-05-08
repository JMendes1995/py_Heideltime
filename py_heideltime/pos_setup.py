import os
from dateutil.parser import parse
import xml.etree.ElementTree as ET
from langdetect import detect
from lang import languages
import codecs
import platform

if __name__ == "__main__":

    check_os = platform.system()

    text = '''
################################
##           MAIN             ##
################################
# Consideration of different timex3-types
# Date
considerDate = true

# Duration
considerDuration = true

# Set
considerSet = true

# Time
considerTime = true

# Temponyms (make sure you know what you do if you set this to "true")
considerTemponym = false

###################################
# Path to TreeTagger home directory
###################################
# Ensure there is no white space in path (try to escape white spaces)
treeTaggerHome = HeidelTime/TreeTagger'''+check_os+'''
# This one is only necessary if you want to process chinese documents.
chineseTokenizerPath = SET ME IN CONFIG.PROPS! (e.g., /home/jannik/treetagger/chinese-tokenizer)

##################################
# paths to JVnTextPro model paths:
##################################
sent_model_path = SET ME IN CONFIG.PROPS! (e.g., /home/jannik/jvntextpro/models/jvnsensegmenter)
word_model_path = SET ME IN CONFIG.PROPS! (e.g., /home/jannik/jvntextpro/models/jvnsegmenter)
pos_model_path = SET ME IN CONFIG.PROPS! (e.g., /home/jannik/jvntextpro/models/jvnpostag/maxent)

#####################################################
# paths to Stanford POS Tagger model or config files:
#####################################################
model_path = SET ME IN CONFIG.PROPS! (e.g., /home/jannik/stanford-postagger-full-2014-01-04/models/arabic.tagger)
# leave this unset if you do not need one (e.g., /home/jannik/stanford-postagger-full-2014-01-04/tagger.config)
config_path = 

########################################
## paths to hunpos and its tagger files:
########################################
hunpos_path = SET ME IN CONFIG.PROPS! (e.g., /home/jannik/hunpos)
hunpos_model_name = SET ME IN CONFIG.PROPS! (e.g., model.hunpos.mte5.defnpout)



# DO NOT CHANGE THE FOLLOWING
################################
# Relative path of type system in HeidelTime home directory
typeSystemHome = desc/type/HeidelTime_TypeSystem.xml

# Relative path of dkpro type system in HeidelTime home directory
typeSystemHome_DKPro = desc/type/DKPro_TypeSystem.xml

# Name of uima-context variables...
# ...for date-consideration
uimaVarDate = Date

# ...for duration-consideration
uimaVarDuration = Duration

# ...for language
uimaVarLanguage = Language

# ...for set-consideration
uimaVarSet = Set

# ...for time-consideration
uimaVarTime = Time

# ...for temponym-consideration
uimaVarTemponym = Temponym

# ...for type to process
uimaVarTypeToProcess = Type

'''

    f = codecs.open("config.props", "w+", "utf-8")
    f.truncate()
    f.write(text)
    f.close()
