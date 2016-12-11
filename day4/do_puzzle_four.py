from collections import Counter

def get_most_common_five(mcl_en):
    result = {}
    v_list = set()
    for k, v in mcl_en.items():
        v = str(v)
        v_list.add(v)
        if v in result.keys():
            result[v] = ''.join(sorted(result[v] + k))
        else:
            result[v] = k

    v_list = sorted(v_list, reverse=True)
    mcf = ''
    for v in v_list:
        mcf = mcf + result[v]
    return mcf[:5]

def rotate_name(name, rot):
    rot = rot % 26
    zero = ord('a')
    result = ''
    for c in name:
        if c == '-':
            result = result + ' '
        else:
            o = ord(c) + rot
            if o >= zero + 26:
                o = o - 26

            result = result + chr(o)
    return result


total = 0
for line in open('puzzle_four_data.txt', 'r'):
    # remove trailing return
    line = line[:-1]

    if line:
        # most common letters
        mcl = line[-6:-1]

        # sector id
        si = int(line[-10:-7])

        # most common five letters in the encrypted name
        mcl_en = Counter(line[:-10].replace('-',''))
        mcf = get_most_common_five(mcl_en)

        if mcf == mcl:
            total = total + si

        # decrypted name
        dn = rotate_name(line[:-10], si)

        if 'pole' in dn:
            print(dn, si)

print(total)





