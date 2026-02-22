import { useState } from "react";
import FeedbackForm from "./components/FeedbackForm";
import FeedbackList from "./components/FeedbackList";

function App() {
  const [refreshTrigger, setRefreshTrigger] = useState(0);

  const handleFeedbackSubmitted = () => {
    // Trigger a refresh of the feedback list
    setRefreshTrigger((prev) => prev + 1);
  };

  return (
    <div className="container">
      <h1>📚 Full Stack Feedback Application</h1>

      <div className="form-section">
        <p style={{ color: "#666", marginBottom: "20px", lineHeight: "1.6" }}>
          Welcome to our educational full-stack application! This is a learning
          platform designed to demonstrate how data flows through a modern web
          application:
          <br />
          <strong>
            Frontend (React) → Backend (Flask) → Database (PostgreSQL)
          </strong>
        </p>
      </div>

      <h2>✍️ Submit Your Feedback</h2>
      <FeedbackForm onFeedbackSubmitted={handleFeedbackSubmitted} />

      <h2>👁️ View All Feedback</h2>
      <FeedbackList refreshTrigger={refreshTrigger} />
    </div>
  );
}

export default App;
