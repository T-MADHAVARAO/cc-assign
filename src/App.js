import { BrowserRouter, Routes, Route } from "react-router-dom";

import HomePage from "./components/HomePage";

import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" Component={HomePage} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
