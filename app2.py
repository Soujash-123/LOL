import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name = "dyxjcp6yo",
    api_key = "822825747231535",
    api_secret = "REloY6Xf4r-i_TrHJfJFN36j-dU",
    secure = True
)

def upload_video(video_path, resource_type="video", **options):
    upload_options = {
        'folder': 'videos/',  
        'resource_type': resource_type,
    }
    
    upload_options.update(options)

    try:
        result = cloudinary.uploader.upload(video_path, **upload_options)
        print(f"Video uploaded successfully. URL: {result['secure_url']}")
        return result
    except Exception as e:
        print(f"Upload failed: {str(e)}")
        return None

if __name__ == "__main__":
    video_file = "video1.mp4"
    result = upload_video(video_file)
 