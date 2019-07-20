import concurrent.futures
import hashlib

"""
reference
http://qiita.com/kokumura/items/2e3afc1034d5aa7c6012
"""

def digest(t): # 適当にCPU資源を消費するための関数
    hash = hashlib.sha256()
    for i in range(t*1000000):
        hash.update(bytes('hogehoge','utf-8'))
    return hash.hexdigest()

if __name__=='__main__':

    task_list = [1,1,1,2,2,3]

    # Executorオブジェクトを作成
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=4)

    # Executorオブジェクトにタスクをsubmitし、同数だけfutureオブジェクトを得る。
    # タスクの実行は、submit()を呼び出した瞬間から開始される。
    futures = [executor.submit(digest,t) for t in task_list]

    # 各futureの完了を待ち、結果を取得。
    # as_completed()は、与えられたfuturesの要素を完了順にたどるイテレータを返す。
    # 完了したタスクが無い場合は、ひとつ完了するまでブロックされる。
    for future in concurrent.futures.as_completed(futures):
        print(future.result()) # digest()の戻り値が表示される。

    # すべてのタスクの完了を待ち、後始末をする。
    # 完了していないタスクがあればブロックされる。
    # (上でas_completedをすべてイテレートしているので、実際にはこの時点で完了していないタスクは無いはず。)
    executor.shutdown()
