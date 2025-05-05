from flask import Blueprint, request, jsonify
import yt_dlp

downloads_bp = Blueprint('downloads', __name__)

@downloads_bp.route('/download', methods=['POST'])
def download():
    data = request.json
    if not data or 'video_url' not in data:
        return jsonify({'error': 'Missing video_url'}), 400

    video_url = data['video_url']

    ydl_opts = {'outtmpl': '/app/data/videos/%(title)s.%(ext)s'}

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Download started', 'video_url': video_url}), 202
