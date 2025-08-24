import os
import sys
from datetime import datetime

def write_log(problem_id, problem_name, message, level="INFO"):
    # 建立資料夾，例如 "1_two_sum"
    folder_name = f"{problem_id}_{problem_name.replace(' ', '_').lower()}"
    os.makedirs(folder_name, exist_ok=True)

    # Log 檔路徑
    log_path = os.path.join(folder_name, "log.txt")

    # 產生 log 格式
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{level}] {message}\n"

    # 寫入 log 檔案
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(log_line)

    print(f"✅ 已寫入 {log_path}")

def main():
    if len(sys.argv) < 3:
        print("用法: python leetcode_logger.py <題號> <題目名稱>")
        print("例如: python leetcode_logger.py 1 'Two Sum'")
        return

    problem_id = sys.argv[1]
    problem_name = sys.argv[2]

    print(f"📘 題目 {problem_id}: {problem_name}")

    # 先輸入 Note
    note = input("📝 請輸入 Note: ")
    if note.strip():
        write_log(problem_id, problem_name, f"Note: {note}", level="INFO")

    # 接著輸入其他紀錄
    print("👉 輸入其他紀錄（每行會單獨存一筆，輸入空白行結束）：")
    while True:
        line = input("> ")
        if line.strip() == "":
            break
        write_log(problem_id, problem_name, line, level="INFO")

if __name__ == "__main__":
    main()
