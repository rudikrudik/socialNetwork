import { Navigate, useLocation } from 'react-router-dom';
import Cookies from "js-cookie";


const ProtectedRoute = ({ children }) => {
    const token = Cookies.get('user_access_token');
    console.log(Cookies)
    const location = useLocation();

    if (!token) {
        return <Navigate to="/login" state={{ from: location }} replace />;
    }

    return children;
};

export default ProtectedRoute;