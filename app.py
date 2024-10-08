from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'

@app.route('/get_transcript')
def get_transcript():
    video_id = request.args.get('videoId')
    if not video_id:
        return "No video ID provided", 400

    try:
        cap = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join(c['text'] for c in cap)
        return render_template_string('''
            <h1>Transcript</h1>
            <p>{{ transcript }}</p>
            <a href="/">Go Back</a>
        ''', transcript=text)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500


if __name__ == "__main__":
    app.run()
