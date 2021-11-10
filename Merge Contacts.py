def rev(L):
    for i in range(0, len(L) // 2):
        # Switches elements about the "mirror"
        # Discussed in Live Lectures
        (L[i], L[len(L) - i - 1]) = (L[len(L) - i - 1], L[i])
    return L


# Merges two sorted lists into a sorted list
def merge(L1, L2):
    # ASSERT: L1 & L2 are established.
    output = []
    if L1 == [] and L2 == []:
        return []
    else:
        # ASSERT: output contains list sorted in reverse order
        while True:  # Loop will run until return is executed
            if L1 == [] and L2 != []:
                # ASSERT: L1 = [], L2 = [b1,..bk], output = [t1,...a1]
                # ASSERT: b1,...bk < t for all t in output
                output.extend(rev(L2))
                # output = [t1...a1,bk,..b1]
                return rev(output)
            elif L1 != [] and L2 == []:
                # ASSERT: L1 = [a1,...ak], L2 = [], output = [t1,...b1]
                # ASSERT: a1,...ak < t for all t in output
                output.extend(rev(L1))
                # output = [t1...b1,ak,..a1]
                return rev(output)
            else:
                # ASSERT: L1 = [a1,...ak], L2 = [b1,...bk]
                # output = [t1,t2,...]
                if L1[-1] > L2[-1]:
                    x = L1.pop()
                    output.append(x)
                    # ASSERT: L1 = [a1,...ak-1], L2 = [b1,...bk]
                    # output = [t1,t2,...ak]
                else:
                    # ASSERT: L1 = [a1,...ak], L2 = [b1,...bk]
                    # output = [t1,t2,...]
                    y = L2.pop()
                    output.append(y)
                    # ASSERT: L1 = [a1,...ak-1], L2 = [b1,...bk]
                    # output = [t1,t2,...ak]


def mergeSort(L):
    # ASSERT: List L is established.
    if L == []:
        return []
    else:
        sortL = []
        # ASSERT: List sortL is established
        # L = [l1,l2,...ln]
        for i in L:
            sortL.append([i])
        # ASSERT: sortL = [[l1],[l2],...[ln]]
        while len(sortL) != 1:
            # ASSERT: sortL = [[a1,a2,..],[b1,b2,...],..]
            # INV: sortL is a list of sorted lists
            if len(sortL) % 2 == 0:
                # ASSERT: sortL has even no. of sorted lists
                temp = []
                # ASSERT: Null list temp is established
                for k in range(0, len(sortL), 2):
                    temp.append(merge(sortL[k], sortL[k + 1]))
                # Consecutive elements of sortL are merged and appended to temp
                sortL = temp
            else:
                # ASSERT: sortL has odd no. of sorted lists
                temp = []
                # ASSERT: Null list temp is established.
                for k in range(0, len(sortL) - 1, 2):
                    temp.append(merge(sortL[k], sortL[k + 1]))
                # Consecutive elements of sortL are merged and appended to temp
                # Since odd no of lists, last list is not merged
                temp.append(sortL[-1])
                sortL = temp
        return sortL[0]


def mergeContacts(ls):
    # ASSERT: List ls = [("B","b"),("A","a"),...] is established
    pList = mergeSort(ls)
    # ASSERT: pList is established
    # pList = [("A","a"),("B","b"),...]
    # INV: Same name are consecutive in pList
    output = []
    k = 0
    # ASSERT: k is established
    # No of elements of pList iterated over = k
    while k < len(pList):
        # INV: Output is list of (name,list of email addresses) of all before k
        # ASSERT: pList[k] is a tuple ("X","x")
        hd = (pList[k])[0]
        temp = [(pList[k])[1]]
        count = 0
        # No of "extra" contacts of one person = count
        while count < len(pList) - k - 1:
            if (pList[k + count])[0] == (pList[k + count + 1])[0]:
                temp.append((pList[k + count + 1])[1])
                count = count + 1
            else:
                # No further common contacts
                # Since pList is sorted, break
                break
        # ASSERT: To prevent repetition of "extra" contacts
        # Skip those by increasing k by count + 1
        k = k + count + 1
        tup = (hd, temp)
        # Tuple tup = (hd,temp) is established
        # tup contains
        output.append(tup)
    # ASSERT: By INV output is list of (name,list of email addresses) of all
    return output
