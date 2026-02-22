const API_BASE_URL = "http://localhost:5000/api";

/**
 * Fetch all feedback from the backend
 * @returns {Promise<Array>} Array of feedback objects
 */
export async function getAllFeedback() {
  try {
    const response = await fetch(`${API_BASE_URL}/feedback`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching feedback:", error);
    throw error;
  }
}

/**
 * Submit new feedback to the backend
 * @param {Object} feedback - The feedback object containing name, subject, and message
 * @returns {Promise<Object>} The created feedback object with id and timestamp
 */
export async function submitFeedback(feedback) {
  try {
    const response = await fetch(`${API_BASE_URL}/feedback`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(feedback),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(
        errorData.error || `HTTP error! status: ${response.status}`,
      );
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error submitting feedback:", error);
    throw error;
  }
}
