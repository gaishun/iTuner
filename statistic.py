import  os
import  sys


def read_file (filename, seek='', cpu_num = 0):

    cmd = 'cat '+filename+' | grep '+seek+' | awk \'{ for ( i=2; i<='+str(cpu_num)+'; i++ ) {print $i} }\' '
    #print(cmd)
    ans = os.popen(cmd)
    ans= ans.read()
    #print(ans)

    anss = ans.split('\n')
    #print(anss)

    while '' in anss:
        anss.remove('')
    while '0' in anss:
        anss.remove('0')
    #print(anss)

    for i,ans in enumerate(anss):
        if ans[-1] == '\n':
            ans = ans[:-1]
        anss[i] = ans.lstrip(' ')

    #print(anss)

    while '' in anss:
        anss.remove('')
    for i, ans in enumerate(anss):
        anss[i] = int(ans)
    #print(anss)
    return anss


def sum (ans):
    #print(ans)
    res = 0
    for i in ans:
        res+=i
    return res

if __name__ == '__main__':
    file_name = sys.argv[1]
    device = sys.argv[2]
    cpu_num = sys.argv[3]
    ans = read_file(file_name,device,cpu_num)
    # ans = parser(ans)
    print(sum(ans))