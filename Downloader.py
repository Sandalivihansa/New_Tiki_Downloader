import instaloader


# Instagram media yuklab olish funksiyasi
async def download_instagram_media(url):
    loader = instaloader.Instaloader()

    # URL orqali postni olish
    shortcode = url.split("/")[-2]  # URLdan shortcode ajratib olish
    post = instaloader.Post.from_shortcode(loader.context, shortcode)

    media_files = []

    if post.typename == "GraphSidecar":  # Karusel media turi
        for node in post.get_sidecar_nodes():
            if node.is_video:
                media_files.append((node.video_url, 'video/mp4'))
            else:
                media_files.append((node.display_url, 'image/jpeg'))
    else:  # Yagona media (rasm yoki video)
        if post.is_video:
            media_files.append((post.video_url, 'video/mp4'))
        else:
            media_files.append((post.url, 'image/jpeg'))

    return media_files
