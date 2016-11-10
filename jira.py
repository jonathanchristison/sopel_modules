import json
import sys
from sopel.module import commands, NOLIMIT, example, rule
from sopel import web, tools

if sys.version_info.major < 3:
  from urllib2 import HTTPError
  from urlparse import urlparse
else:
  from urllib.request import HTTPError
  from urllib.parse import urlparse


jboss_org_base_url = "https://issues.jboss.org"
jboss_org_rest = jboss_org_base_url + "/rest/api/2/issue/"
jboss_org_case = jboss_org_base_url + "/browse/"

def query_jira(jira_id):
  response = web.get(jboss_org_rest + jira_id)
  response = json.loads(response)
  return "[{0}] {1} - {2}".format(jira_id, response["fields"]["summary"], jboss_org_case + jira_id )

@rule('.*(ENTESB-\d+).*')
def versions(bot, trigger):
  text = trigger.group(1)
  bot.say( query_jira(text) )

