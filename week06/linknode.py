import statistics


class LinkNode():
    """
    链表节点类
    """
    def __init__(self, date):
        self.date = date
        self.next = None


class SigLink():
    """
    self.length   用于记录链表的长度
    self.head     链表的头部
    self.tail     记录链表的尾部
    """
    def __init__(self, item):
        """
        item   一位数组，存放改链表的数组

        """
        self.length = len(item)
        if self.length <= 0:
            return
        i = 0
        self.head = LinkNode(item[i])
        self.tail = self.head
        i += 1                    # 此句不能少
        while i < self.length:
            self.tail.next = LinkNode(item[i])
            self.tail = self.tail.next
            i += 1

    def printlink(self):
        """
            正序打印该链表
        """
        if self.head==None:
            print("该链表为空链表！")
        p=self.head
        while p!=None:
            print(p.dat,end=" ")
            p=p.next

    def getlength(self):
        """
            获取链表的长度
        """
        print("该链表的长度为：",self.length)

    def linkAppend(self,num):
        """在链表尾部追加节点"""
        self.tail.next=LinkNode(num)
        self.tail=self.tail.next
        self.length+=1

    def insertNode(self,index,num):
        """
            在链表中间插入节点
            index：插入节点的序号
            num：插入点的值
        """
        if index>self.length:
            print("index参数超出范围")
            return
        if index==self.length:
            self.linkAppend(num)
            return
        if index==0:
            p=LinkNode(num)
            p.next=self.head
            self.head=p
            self.length+=1
            return
        ptemp=self.head
        while index>1:
            ptemp=ptemp.next
            index-=1
        p=LinkNode(num)
        p.next=ptemp.next
        ptemp.next=p
        self.length+=1


a=[]
flag=""
NodeNum=int(input("请输入节点的个数："))
for i in range(1,NodeNum+1):
    a.append(int(input("您输入的第%d个节点的值为："%i)))

Link=SigLink(a)
number=int(input("请你输入你要执行的次数："))
i=0#标记次数
while i<number:
    operation=input("请输入你要进行的操作名称：")
    name=flag+str(operation)
    i+=1
    if name=="printlink":
        print("遍历的结果为：")
        Link.printlink()
        print("\n")
    elif name=="getlength":
        Link.getlength()
    elif name=="linkAppend":
        num=int(input("请输入你要追加的数字："))
        Link.linkAppend(num)
        print("追加成功！")
        print("追加之后遍历的结果为：")
        Link.printlink()
        print("\n")
    elif name=="insertNode":
        Index=int(input("你要索引的位置为：："))
        NodeNum=int(input("你要在%d插入的数字："%Index))
        Link.insertNode(Index,NodeNum)
        print("插入成功！")
        print("插入之后遍历的结果为：")
        print("\n")
        Link.printlink()
    if name!="printlink" or name!="getlength"or name!="linkAppend" or name!="insertNode":
        print("输入操作名称有误，请重新输入！")


while i>=number:
    print("\n")
    print("执行次数已经达到，结束程序！")
    i=i-1
