txt = """/

=====================================
2017-11-17 10:11:15 0x1568 INNODB MONITOR OUTPUT
=====================================
Per second averages calculated from the last 29 seconds
-----------------
BACKGROUND THREAD
-----------------
srv_master_thread loops: 11 srv_active, 0 srv_shutdown, 4857 srv_idle
srv_master_thread log flush and writes: 4868
----------
SEMAPHORES
----------
OS WAIT ARRAY INFO: reservation count 765
OS WAIT ARRAY INFO: signal count 705
RW-shared spins 0, rounds 1568, OS waits 665
RW-excl spins 0, rounds 3756, OS waits 26
RW-sx spins 1, rounds 30, OS waits 1
Spin rounds per wait: 1568.00 RW-shared, 3756.00 RW-excl, 30.00 RW-sx
------------
TRANSACTIONS
------------
Trx id counter 847890
Purge done for trx's n:o < 843815 undo n:o < 0 state: running but idle
History list length 823
LIST OF TRANSACTIONS FOR EACH SESSION:
---TRANSACTION 284449640549016, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 284449640548144, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
--------
FILE I/O
--------
I/O thread 0 state: wait Windows aio (insert buffer thread)
I/O thread 1 state: wait Windows aio (log thread)
I/O thread 2 state: wait Windows aio (read thread)
I/O thread 3 state: wait Windows aio (read thread)
I/O thread 4 state: wait Windows aio (read thread)
I/O thread 5 state: wait Windows aio (read thread)
I/O thread 6 state: wait Windows aio (write thread)
I/O thread 7 state: wait Windows aio (write thread)
I/O thread 8 state: wait Windows aio (write thread)
I/O thread 9 state: wait Windows aio (write thread)
Pending normal aio reads: [0, 0, 0, 0] , aio writes: [0, 0, 0, 0] ,
 ibuf aio reads:, log i/o's:, sync i/o's:
Pending flushes (fsync) log: 0; buffer pool: 0
3886 OS file reads, 587 OS file writes, 68 OS fsyncs
0.00 reads/s, 0 avg bytes/read, 0.00 writes/s, 0.00 fsyncs/s
-------------------------------------
INSERT BUFFER AND ADAPTIVE HASH INDEX
-------------------------------------
Ibuf: size 1, free list len 147, seg size 149, 162 merges
merged operations:
 insert 423, delete mark 0, delete 0
discarded operations:
 insert 0, delete mark 0, delete 0
Hash table size 2267, node heap has 0 buffer(s)
Hash table size 2267, node heap has 0 buffer(s)
Hash table size 2267, node heap has 0 buffer(s)
Hash table size 2267, node heap has 0 buffer(s)
Hash table size 2267, node heap has 1 buffer(s)
Hash table size 2267, node heap has 1 buffer(s)
Hash table size 2267, node heap has 0 buffer(s)
Hash table size 2267, node heap has 0 buffer(s)
0.00 hash searches/s, 0.00 non-hash searches/s
---
LOG
---
Log sequence number 2038637910
Log flushed up to   2038637910
Pages flushed up to 2038637910
Last checkpoint at  2038637901
0 pending log flushes, 0 pending chkp writes
37 log i/o's done, 0.00 log i/o's/second
----------------------
BUFFER POOL AND MEMORY
----------------------
Total large memory allocated 8585216
Dictionary memory allocated 1621129
Buffer pool size   512
Free buffers       237
Database pages     273
Old database pages 0
Modified db pages  0
Pending reads      0
Pending writes: LRU 0, flush list 0, single page 0
Pages made young 0, not young 0
0.00 youngs/s, 0.00 non-youngs/s
Pages read 3848, created 72, written 528
0.00 reads/s, 0.00 creates/s, 0.00 writes/s
No buffer pool page gets since the last printout
Pages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s
LRU len: 273, unzip_LRU len: 0
I/O sum[0]:cur[0], unzip sum[0]:cur[0]
--------------
ROW OPERATIONS
--------------
0 queries inside InnoDB, 0 queries in queue
0 read views open inside InnoDB
Process ID=2300, Main thread ID=3676, state: sleeping
Number of rows inserted 475, updated 0, deleted 0, read 47828
0.00 inserts/s, 0.00 updates/s, 0.00 deletes/s, 0.00 reads/s
----------------------------
END OF INNODB MONITOR OUTPUT
============================
"""
