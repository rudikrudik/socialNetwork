import { Navigate, useLocation } from 'react-router-dom';
import Cookies from "js-cookie";


const ProtectedRoute = ({ children }) => {
    const token = Cookies.get('token');
    const location = useLocation();

    if (!token) {
        return <Navigate to="/login" state={{ from: location }} replace />;
    }

    return children;
};

export default ProtectedRoute;