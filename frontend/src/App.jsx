import { useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");

  const createShortUrl = async () => {
    const response = await fetch(
      `${import.meta.env.VITE_API_URL}/shorten`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          original_url: url,
        }),
      }
    );

    const data = await response.json();

    setShortUrl(data.short_code);
  };

  return (
    <div>
      <h1>Cloud URL Shortener</h1>

      <input
        type="text"
        placeholder="Enter URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <button onClick={createShortUrl}>
        Shorten
      </button>

      {shortUrl && (
        <p>
          Short URL:
          {import.meta.env.VITE_API_URL}/{shortUrl}
        </p>
      )}
    </div>
  );
}

export default App;