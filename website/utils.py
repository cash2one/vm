
from website.models import Node

def getNodeIdList(my_user):
    company = my_user.company
    #node_list = Node.objects.values('name_id')
    node_list = company.node_set.values('name_id')
    return node_list

def getNetNameList(my_user):
    company = my_user.company
    net_list = company.node_set.values('net_name').distinct()
    return net_list