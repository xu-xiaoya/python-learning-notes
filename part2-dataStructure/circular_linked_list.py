"""循环链表：每个节点的 next 指向下一个，最后一个节点又指回第一个，首尾相连成环。"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def construire_cercle(valeurs):
    """从值列表建一个循环链表，返回第一个节点。"""
    nodes = [Node(v) for v in valeurs]
    n = len(nodes)
    for i in range(n):
        # (i+1) % n：最后一个节点的 next 用取余绕回索引 0，形成环
        nodes[i].next = nodes[(i + 1) % n]
    return nodes[0]


def afficher(depart, limite=10):
    """从 depart 出发，沿 next 走，绕一圈打印出来。"""
    cur = depart
    vus = []
    for _ in range(limite):          # limite 是保险：万一没成环也不会无限循环
        vus.append(cur.val)
        cur = cur.next
        if cur is depart:            # 用 is 判断是否回到起点（同一个对象）
            break
    print("绕圈顺序:", vus, "(然后又回到", depart.val, ")")


def main():
    tete = construire_cercle([1, 2, 3, 4])
    afficher(tete)
    print("第一个节点:", tete.val)
    print("它的下一个:", tete.next.val)
    print("下一个的下一个:", tete.next.next.val)
    print("再下一个的下一个:", tete.next.next.next.val)
    print("绕回来了吗:", tete.next.next.next.next.val, "← 应该又是1")


if __name__ == "__main__":
    main()
