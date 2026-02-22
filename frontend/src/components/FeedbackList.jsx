import { useEffect, useState } from "react";
import { getAllFeedback } from "../api";

export default function FeedbackList({ refreshTrigger }) {
  const [feedbackList, setFeedbackList] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    loadFeedback();
  }, [refreshTrigger]);

  const loadFeedback = async () => {
    setIsLoading(true);
    setError("");

    try {
      const data = await getAllFeedback();
      setFeedbackList(data || []);
    } catch (err) {
      setError("Failed to load feedback. Please try again later.");
      console.error("Error loading feedback:", err);
    } finally {
      setIsLoading(false);
    }
  };

  if (error) {
    return (
      <div className="error" style={{ padding: "20px", textAlign: "center" }}>
        {error}
      </div>
    );
  }

  if (isLoading) {
    return (
      <div className="loading">
        <div className="spinner"></div>
      </div>
    );
  }

  if (feedbackList.length === 0) {
    return (
      <div className="feedback-list">
        <div className="empty-state">
          <div className="empty-state-icon">📝</div>
          <p>No feedback yet. Be the first to share your thoughts!</p>
        </div>
      </div>
    );
  }

  return (
    <div className="feedback-list">
      {feedbackList.map((item) => (
        <div key={item.id} className="feedback-item">
          <div className="feedback-name">👤 {item.name}</div>
          <div className="feedback-subject">📌 {item.subject}</div>
          <div className="feedback-message">{item.message}</div>
          <div className="feedback-timestamp">
            ⏰ {new Date(item.created_at).toLocaleString()}
          </div>
        </div>
      ))}
    </div>
  );
}
