const BASE_URL = "http://127.0.0.1:8000/api";

/**
 * Helper to handle standard API headers with token authentication.
 * For the hackathon demo, we will hardcode a baseline user login session,
 * but this is ready to scale to dynamic tokens.
 */
const getHeaders = (token) => ({
  "Content-Type": "application/json",
  ...(token && { Authorization: `Token ${token}` }),
});

export const api = {
  // Fetch the student profile statistics (Level, XP, Grade)
  getProfile: async (token) => {
    const response = await fetch(`${BASE_URL}/auth/profile/`, {
      method: "GET",
      headers: getHeaders(token),
    });
    if (!response.ok) throw new Error("Failed to load profile details.");
    return response.json();
  },

  // Trigger the background Celery job for AI routing
  triggerAI: async (token) => {
    const response = await fetch(`${BASE_URL}/career/generate/`, {
      method: "POST",
      headers: getHeaders(token),
    });
    if (!response.ok) throw new Error("Failed to initialize AI tracking matrix.");
    return response.json(); // Returns { task_id: "..." }
  },

  // Poll the status of the background task
  checkAIStatus: async (token, taskId) => {
    const response = await fetch(`${BASE_URL}/career/status/${taskId}/`, {
      method: "GET",
      headers: getHeaders(token),
    });
    if (!response.ok) throw new Error("Error checking background task execution state.");
    return response.json(); // Returns { status: "SUCCESS" | "PENDING", result: ... }
  }
};