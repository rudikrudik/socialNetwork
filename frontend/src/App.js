import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import "./index.css"
import Header from "./Layouts/Header";
import Main from "./Layouts/Main";
import LeftMenu from "./Layouts/LeftMenu";
import RightMenu from "./Layouts/RightMenu";
import Profile from "./Layouts/Profile";
import Login from "./Layouts/Login";
import ProtectedRoute from "./Components/ProtectedRoute";
import Logout from "./Layouts/Logout";
import Posts from "./Layouts/Posts";

function App() {
    return (
        <div className="wrap">
            <Router>
                <Header />
                <div className="wrap_content">
                    <LeftMenu/>
                    <Routes>
                        <Route exact path="/" element={<ProtectedRoute><Main /></ProtectedRoute>} />
                        <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>}/>
                        <Route path="/posts" element={<ProtectedRoute><Posts /></ProtectedRoute>}/>
                        <Route exact path="/login" element={<Login />} />
                        <Route exact path="/logout" element={<Logout />} />
                    </Routes>
                    <RightMenu/>
                </div>
            </Router>
        </div>
    );
}

export default App;

