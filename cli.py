import argparse
from emotion_inference.inference import predict_emotion

def main():
    parser = argparse.ArgumentParser(description="Emotion Inference CLI Tool")
    parser.add_argument('--input', type=str, help="Text input to predict emotion")
    parser.add_argument('--kaggle', action='store_true', help="Show your Kaggle ID")

    args = parser.parse_args()

    if args.kaggle:
        print("yourkaggleid")  # Replace with your actual Kaggle ID
    elif args.input:
        emotion = predict_emotion(args.input)
        print(emotion)
    else:
        parser.print_help()