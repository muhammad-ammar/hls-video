# hls-video
Serve and play hls videos



**Usage Instructions**


```
git clone https://github.com/muhammad-ammar/hls-video.git
```

**Serve HLS Videos**

```python video.py --dir '~/Documents/hls_videos' --port 8989```

Now the video server is running. Visit http://127.0.0.1:8989/ and you should see all the files inside the directroy. Right click on a `m3u8` file and click on `Copy Link Address`.

**Play HLS Videos**

```
1. Open client.html in browser.
2. Input a HLS video url(copied in the Serve HLS Videos section) in the input field and press Play Video button.
```
