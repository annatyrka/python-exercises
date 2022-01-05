import re
agentNames = re.compile(r'Agent \w*')
mo = agentNames.sub(
    'CENSORED', "Agent Alice gave the secret documents to Agent Bob.")
print(mo)

agentNames = re.compile(r'Agent (\w)\w*')
mo2 = agentNames.sub(
    r'\1****', "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.")
print(mo2)
