#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cisco_conf = CiscoConfParse("cisco_ipsec.txt")

crypto_maps = cisco_conf.find_objects(r"^crypto map CRYPTO")


# Lesson 8
for cm in crypto_maps:
 print(cm.children)

# Lesson 9

pfs_group2 = cisco_conf.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")
for p in pfs_group2:
    print(p)
# Lesson 10

not_aes = cisco_conf.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES")
for n in not_aes:
    print(n.text)
    transform_set = n.children[1]
    print(transform_set.text)
    

