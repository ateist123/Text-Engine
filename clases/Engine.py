class Engine():
    def __init__():
        pass

    def react(r_dict,r_dict_1):
        print()
        for x in range(0,len(r_dict)):
            print(rdict[x])
        print('\n'*3)
        act = input('Action button: ')
        a_code = -1
        for x in range(0,len(r_dict_1)):
            if act==r_dict_1[x]:
                a_code = x
                break
        return a_code

    def write_info(info):
        linfo = len(info)+10
        print('*'*linfo)
        print('  '+info)
        print('*'*linfo)

    def act_frame(self,info, r_dict, r_dict_1):
        self.write_info(info)
        return self.react(r_dict, r_dict_1)

    def showInventory(object):

