import "./index.css";

const HomePage = () => (
  <div className="App">
    <h1 className="details">MY ABOUT </h1>
    <div className="data">
      <div className="profile-img-sec">
        <div className="profile-cont">
          <img
            src="https://res.cloudinary.com/dmhifljqo/image/upload/v1702889508/898de90d-8fc7-45e2-99bc-438bdd69b9eb_1_dtzi0y.jpg"
            alt="profile"
            className="profile"
          />
        </div>
      </div>
      <h1 className="item">
        Name : <span>TARRA MADHAVA RAO</span>
      </h1>
      <h1 className="item">
        Graduation PassOut Year: <span>JULY-2024</span>
      </h1>
      <h1 className="item">Technologies/ Language Used: </h1>
      <ul className="technologies">
        <li>HTML</li>
        <li>CSS</li>
        <li>BootStrap</li>
        <li>JavaScript</li>
        <li>ReactJS</li>
        <li>Python</li>
        <li>SQLite</li>
        <li>Node.JS (Express.js)</li>
      </ul>
    </div>
  </div>
);

export default HomePage;
