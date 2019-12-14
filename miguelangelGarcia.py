
"""
~~~Going to open file and identify original DUNS numbers from duplicates~~~
1. Will open file
2. Will grab DUNS number and add it to dict if its not there.
3. will save name down along with DUNS
4. Any duplicates will not be added. S
5. Should slim down list
"""


from itertools import islice
import csv

co_dict_name = {}
co_dict_bus_act = {}
bus_act_uses = {}


start_index = 0
stop_index = 3886

def writer(name_fix, duns, activity, sec):
    f.write(str(name_fix) + ',')
    f.write(str(duns) + ',')
    f.write(str(activity) + ',')
    f.write(str(sec) + ',')
    f.write('\n')


with open('uniqueidneeded.csv', 'r') as unique_csv: # opens files to compare DUNS numbers

    reader_csv = csv.reader(unique_csv) # creates new output file

    file_name = 'uniqueresults.csv'
    f = open(file_name, 'w')
    #headers = "Applicant_Name, DUNS, Global_Parent_DUNS\n"
    #f.write(headers)

    Name, DUNS, Activity = [], [], []

    i = 0
    uses = 0
    for line in islice(reader_csv, start_index, stop_index):
        name = line[0]
        duns = line[1]
        activity = line[2]
        name_fix = name.replace(',', '').replace('-', ' ').replace('.', '').upper() # .strip(' ') (test1) [54]
        # .upper() is test 2 []

        #print(name_fix)
        print('LINE', end = '')
        print(line)

        if duns not in DUNS:
            DUNS.append(duns)
            print('ALL', end = '')
            print(DUNS)

            co_dict_bus_act.update({duns: activity})

            writer(name_fix, duns, activity, 1)

            keeper = (name_fix + duns + activity)
            print(keeper)

            bus_act_uses.update({keeper: i})

            i += 1
            ken = len(bus_act_uses)
            print('ken: ', end = '')
            print(ken)

        elif duns in DUNS:
            Name.append(name_fix)

            keeper2 = (name_fix + duns + activity)

            #if name_fix in Name:

            if keeper2 not in bus_act_uses:
                print('ITS KENNNNNN')
                print(ken)

                # and co_dict_bus_act[duns] != activity:
                print('i am here')
                i += 1
                bus_act_uses.update({keeper2: i})

                co_dict_name.update({duns: name_fix})

                print(co_dict_bus_act[duns])
                print(activity)

                #if co_dict_bus_act[duns] == activity:
                    # print(co_dict_bus_act[duns])
                    # print(activity)

            #if keeper == present and co_dict_bus_act[duns] != activity: # and co_dict_name[name_fix] == duns: # and duns == :
                # print(name)
                # print(name)
                # print('next')
                # print('keeper: ', end = '')
                # print(bus_act_uses[keeper])

                #if name_fix in Name and co_dict_bus_act[duns] != activity:

                writer(name_fix, duns, activity, 2) # added sec to understand whereour problem was coming from
                    # sec 2 was the problem, could compare 2 diff values, not 3


                    # added this because multipls of the same 2nd or 3rd other business activities were being written creating multiples
                print(keeper)
                print(bus_act_uses[keeper])
                print(bus_act_uses)
                print(ken)

            elif keeper2 in bus_act_uses:
                pass

            else:
                pass


            #if co_dict_name[duns] != name_fix: # and :
                #writer(name_fix, duns, activity, 3)
                #print(name + duns + activity)



    f.close()
