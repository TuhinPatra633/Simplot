import argparse
import json
import pandas as pd
from utils.llm_utils import pred_to_md, calculate_QA
from utils.llm_prompts import prompt
import os

def main(args):
    if args.qa_type == 'human':
        qa_path = f"./data/test1/test_human1.json"
    elif args.qa_type == 'augmented':
        qa_path = f"./data/test1/test_augmented.json"
    else:
        raise ValueError('[ERROR] QA type not recognized')

    args.qa = json.load(open(qa_path))
    print(f"[INFO] Total QA entries loaded: {len(args.qa)}")

    pred = pd.read_csv(args.prediction)
    pred['md'] = pred['pred'].apply(pred_to_md)
    args.pred = pred
    print(f"[INFO] Predictions loaded: {len(pred)} rows")

    qa_list = []
    total_errors = 0

    for index in range(len(args.qa)):
        try:
            result = prompt(args, index, suppress_errors=True)
            if result:
                qa_list.append(result)
        except Exception as e:
            print(f"[ERROR] Failed to process index {index}: {e}")
            total_errors += 1

    if not qa_list:
        raise ValueError("[ERROR] No results were collected. Check your prompt function or data.")

    qa_results = pd.DataFrame(qa_list)
    print(f"[INFO] QA Results DataFrame created with {len(qa_results)} rows")

    if 'correct' not in qa_results.columns:
        raise KeyError("[ERROR] 'correct' column is missing in QA results")

    qa_results, errors = calculate_QA(qa_results)
    qa_results.to_csv('./result/qa_results.csv', index=False)
    print("[INFO] QA results saved to ./result/qa_results.csv")

    print(f"[INFO] Total Errors: {total_errors}")
    print(f"[INFO] Total Questions: {len(qa_results)}")
    print(f"[INFO] Accuracy: {qa_results['correct'].mean()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='QA')
    parser.add_argument('--qa_type', type=str, default='human', help='Type of QA')
    parser.add_argument('--prediction', type=str, default='./result/prediction.csv', help='Path to prediction.csv')
    parser.add_argument('--img_path', type=str, default='./data/test/png/', help='Path to chart images')
    parser.add_argument('--json_path', type=str, default='./data/test/annotations/', help='Path to JSON files')
    parser.add_argument('--temperature', type=float, default=0.1, help='Temperature')
    parser.add_argument('--api_key', type=str, default=os.getenv("GEMINI_API_KEY"), help='Gemini API key')
    args = parser.parse_args()
    main(args)
