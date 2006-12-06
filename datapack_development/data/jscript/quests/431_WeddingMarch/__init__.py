# Created by CubicVirtuoso
# Any problems feel free to drop by #l2j-datapack on irc.freenode.net
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

MELODY_MAESTRO_KANTABILON_ID = 31042
SILVER_CRYSTAL_ID = 7540
LIENRIKS_ID = 20786
LIENRIKS_LAD_ID = 20787
WEDDING_ECHO_CRYSTAL_ID = 7062

class Quest (JQuest) :

 def __init__(self,id,name,descr,party): JQuest.__init__(self,id,name,descr,party)
 
 def onEvent (self,event,st) :
     htmltext = event
     cond = st.getInt("cond")
     if event == "1" and cond == 0 :
         htmltext = "31042-02.htm"
         st.set("cond","1")
         st.setState(STARTED)
         st.playSound("ItemSound.quest_accept")
     elif event == "3" and st.getQuestItemsCount(SILVER_CRYSTAL_ID) == 50 :
         st.giveItems(WEDDING_ECHO_CRYSTAL_ID,25)
         st.takeItems(SILVER_CRYSTAL_ID,50)
         htmltext = "31042-05.htm"
         st.playSound("ItemSound.quest_finish")
         st.exitQuest(1)
     return htmltext
 
 def onTalk (Self,npc,st):
     npcId = npc.getNpcId()
     htmltext = "<html><head><body>I have nothing to say you</body></html>"
     cond = st.getInt("cond")
     id = st.getState()
     if id == CREATED :
         htmltext = "31042-01.htm"
     elif cond == 1 :
         htmltext = "31042-03.htm"
     elif cond == 2 :
         htmltext = "31042-04.htm"
     return htmltext
 
 def onKill(self,npc,st):
     count = st.getQuestItemsCount(SILVER_CRYSTAL_ID)
     if st.getInt("cond") == 1 and count < 50 :
             st.giveItems(SILVER_CRYSTAL_ID,1)
             if count == 49 :
                 st.playSound("ItemSound.quest_middle")
                 st.set("cond","2")
             else :
                 st.playSound("ItemSound.quest_itemget")
     return
 
QUEST       = Quest(431,"431_WeddingMarch","Wedding March",True)
CREATED     = State('Start', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)

QUEST.setInitialState(CREATED)
QUEST.addStartNpc(31042)

CREATED.addTalkId(31042)
COMPLETED.addTalkId(31042)

STARTED.addTalkId(31042)

STARTED.addKillId(20786)
STARTED.addKillId(20787)

STARTED.addQuestDrop(20786,SILVER_CRYSTAL_ID,1)

print "importing quests: 431: Wedding March"
