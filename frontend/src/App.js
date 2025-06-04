import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import "./index.css"
import Header from "./Layouts/Header";
import Main from "./Layouts/Main";
import LeftMenu from "./Layouts/LeftMenu";
import RightMenu from "./Layouts/RightMenu";
import Profile from "./Layouts/Profile";
import Login from "./Layouts/Login";

function App() {
    return (
        <div className="wrap">
            <Router>
                <Header />
                <div className="wrap_content">
                    <LeftMenu/>
                    <Routes>
                        <Route exact path="/" element={<Main />} />
                        <Route exact path="/profile" element={<Profile />} />
                        <Route exact path="/login" element={<Login />} />
                    </Routes>
                    <RightMenu/>
                </div>
            </Router>
        </div>
    );
}

export default App;

