import { Navigate, useLocation } from 'react-router-dom';
import Cookies from "js-cookie";


const ProtectedRoute = ({ children }) => {
    const token = Cookies.get('token');
    console.log("USER ID: ", Cookies.get('user_id'));
    const location = useLocation();

    if (!token) {
        return <Navigate to="/login" state={{ from: location }} replace />;
    }

    return children;
};

export default ProtectedRoute;