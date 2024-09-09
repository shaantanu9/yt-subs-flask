from flask import Flask, request, render_template_string
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/get_transcript" method="get">
            <label for="videoId">YouTube Video ID:</label>
            <input type="text" id="videoId" name="videoId" required>
            <input type="submit" value="Get Transcript">
        </form>
    '''

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

if __name__ == '__main__':
    app.run(debug=True)
