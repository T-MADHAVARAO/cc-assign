import { Link } from "react-router-dom";
const Resume = () => (
  <div className="App">
    <h1>My Resume</h1>
    <a href="https://apricot-marielle-54.tiiny.site" target="blank">
      Open and Download MY RESUME
    </a>
    <div className="back">
      <Link to="/">
        <button>Home</button>
      </Link>
    </div>
  </div>
);

export default Resume;
