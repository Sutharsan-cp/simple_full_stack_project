import { useState } from "react";
import { submitFeedback } from "../api";

export default function FeedbackForm({ onFeedbackSubmitted }) {
  const [formData, setFormData] = useState({
    name: "",
    subject: "",
    message: "",
  });

  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const [successMessage, setSuccessMessage] = useState("");

  const validateForm = () => {
    const newErrors = {};

    if (!formData.name.trim()) {
      newErrors.name = "Name is required";
    }

    if (!formData.subject.trim()) {
      newErrors.subject = "Subject is required";
    }

    if (!formData.message.trim()) {
      newErrors.message = "Message is required";
    }

    if (formData.message.trim().length < 10) {
      newErrors.message = "Message must be at least 10 characters long";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
    // Clear error for this field when user starts typing
    if (errors[name]) {
      setErrors((prev) => ({
        ...prev,
        [name]: "",
      }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    setIsLoading(true);
    setSuccessMessage("");

    try {
      await submitFeedback(formData);
      setSuccessMessage("Feedback submitted successfully! 🎉");
      setFormData({
        name: "",
        subject: "",
        message: "",
      });

      // Notify parent component
      if (onFeedbackSubmitted) {
        onFeedbackSubmitted();
      }

      // Clear success message after 3 seconds
      setTimeout(() => setSuccessMessage(""), 3000);
    } catch (error) {
      setErrors({
        submit: error.message || "Failed to submit feedback. Please try again.",
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form className="form-section" onSubmit={handleSubmit}>
      {successMessage && <div className="success">{successMessage}</div>}

      {errors.submit && <div className="error">{errors.submit}</div>}

      <div className="form-group">
        <label htmlFor="name">Your Name</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="Enter your name"
          disabled={isLoading}
        />
        {errors.name && <div className="error">{errors.name}</div>}
      </div>

      <div className="form-group">
        <label htmlFor="subject">Subject</label>
        <input
          type="text"
          id="subject"
          name="subject"
          value={formData.subject}
          onChange={handleChange}
          placeholder="What is your feedback about?"
          disabled={isLoading}
        />
        {errors.subject && <div className="error">{errors.subject}</div>}
      </div>

      <div className="form-group">
        <label htmlFor="message">Message</label>
        <textarea
          id="message"
          name="message"
          value={formData.message}
          onChange={handleChange}
          placeholder="Share your thoughts, suggestions, or feedback..."
          disabled={isLoading}
        />
        {errors.message && <div className="error">{errors.message}</div>}
      </div>

      <button type="submit" disabled={isLoading}>
        {isLoading ? "Submitting..." : "Submit Feedback"}
      </button>
    </form>
  );
}
