import demowlcutils
from demowlcutils import ppxml, WLC_login
from pprint import pprint as pp 
from lxml import etree
from lxml.builder import E 

wlc = WLC_login()

set_trans = E.TRANSACTION({'tid': '0'},
  E.SESSION,
  E.SET
  )

add_vlan_ele = E('VLAN-TABLE',
  E.VLAN({'number': '100', 'name': 'Jeremy', 'state': 'ACTIVE', 'tunnel-affinity': '5'},
    E('VLAN-IP', {'vrouter': 'local'}),
    E('VLAN-MEMBER-TABLE'),
    E('VLAN-FDB', {'aging-time': '300'},
      E('VLAN-FDB-TABLE')
    ),
    E('VLAN-IGMP',{ 'enabled':'YES', 
                    'proxy-report':'YES',
                    'querier-enabled':'NO', 
                    'mrouter-solicitation': "NO", 
                    'igmp-version':"2",
                    'mrsol-interval': "30",
                    'query-interval': "125",
                    'other-querier-interval': "255",
                    'query-response-interval': "100",
                    'last-member-query-interval':"10",
                    'robustness-value':"2"
                  }),
    E('VLAN-STP',{'enabled':"NO",'instance':"100"})
  ))

# insert the data into the 'SET' node-set

set_trans.find('SET').append( add_vlan_ele )

# now perform the transaction

r = wlc( set_trans )
