import sys
import importlib
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
if sys.version_info < (3, 9):
    import typing
    from typing import Optional

    def _fix_typing():
        typing.Optional = lambda x: typing.Union[x, None]

    _fix_typing()

def run_solution(problem_number: int, solution_number: int):
    """執行 `題號/s{第 i 個解}.py` 的 `test()`"""
    
    module_name = f"questions.{problem_number}.s{solution_number}"  # 例如 '437.s1'
    
    try:
        solution_module = importlib.import_module(module_name)
        
        if hasattr(solution_module, "test"):
            print(f"Running test for {module_name}...\n")
            solution_module.test()
        else:
            print(f"Error: {module_name} 沒有 `test()` 方法！")
    
    except ModuleNotFoundError:
        print(f"Error: 找不到 `{module_name}.py`，請確認檔案是否存在！")
    except Exception as e:
        print(f"Error: 執行 `{module_name}.test()` 發生錯誤\n{e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python runner.py <題號> <第幾個解>")
    else:
        problem_number = sys.argv[1]
        solution_number = sys.argv[2]
        
        run_solution(problem_number, solution_number)
