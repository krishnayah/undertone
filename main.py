import undertone

# Main loop
while True:
    print("-----------------")
    print("--Adding Videos--")
    print("-----------------")
    print(" ")
    print("Enter the URLs you'd like to add. When you're done, leave it blank, or type 'no'")

    videos = []
    answer = ' '
    while answer.lower() not in ['n', 'no', '', -1]:
        url = input("Enter a video URL: ")
        videos.append(url)
        answer = url
    videos = videos[:-1]

    print("Videos added: ", videos)

    print(" ")

    print("-------------------------------------------")
    print("--What size model would you like to use?--")
    print("-------------------------------------------")

    print("small, base, large")

    answer = input("Enter the size of the model you'd like to use: ")
    match answer.lower():
        case "small":
            size = "small"
        case "base":
            size = "base"
        case "large":
            size = "large-v3"
        case _:
            print("Invalid size. Defaulting to large.")
            size = "large"

    undertone.download_model(size)

    for video in videos:
        try:
            filename = undertone.download_video(video)
            undertone.run_model(filename, size)
        except Exception as e:
            print(f"Error processing video: {e}")
            continue
