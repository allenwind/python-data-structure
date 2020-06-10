#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int m_nValue;
    ListNode* m_pNext;
};

ListNode* CreateListNode(int value)
{
    ListNode* pNode = new ListNode();
    pNode->m_nValue = value;
    pNode->m_pNext = nullptr;
}

void ConnectListNodes(ListNode* pCurrent, ListNode* pNext)
{
    if(pCurrent == nullptr)
    {
        exit(1);
    }

    pCurrent->m_pNext = pNext;
}

void PrintList(ListNode* head)
{
    ListNode* pNode = pHead;
    while(pNode != nullptr)
    {
        printf("%d\t", pNode->m_nValue);
        pNode = pNode->m_pNext;
    }
}

void AddToTail(ListNode** pHead, int value)
{

}

void RemoveNode(ListNode** pHead, int value)
{
    
}

void DestroyList(ListNode* pHead)
{
    ListNode* pNode = pHead;
    while(pNode != nullptr)
    {
        pHead = pHead->m_pNext;
        delete pNode;
        pNode = pHead;
    }
}