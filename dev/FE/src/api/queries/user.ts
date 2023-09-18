import {
  getUserArtist,
  getUser,
  getUserTotalCapital,
  getUserCapital,
  // getUserCheckId,
  // userSignup,
  // userLogin,
} from '../user';

const getUserArtistQuery = (userNo: string) => {
  return {
    queryKey: ['getArtist', userNo],
    queryFn: getUserArtist,
  };
};

const getUserTotalCapitalQuery = () => {
  return {
    queryKey: ['getTotalCapital'],
    queryFn: getUserTotalCapital,
  };
};

const getUserQuery = () => {
  return {
    queryKey: ['getUser'],
    queryFn: getUser,
  };
};

// 특정 아이의 재무 상태표
const getUserCapitalQuery = (userNo: number) => {
  return {
    queryKey: ['getUserCapital', userNo],
    queryFn: getUserCapital,
  };
};

export {
  getUserArtistQuery,
  getUserQuery,
  getUserTotalCapitalQuery,
  getUserCapitalQuery,
  // getUserCheckIdQuery,
  // userSignupQuery,
  // userLoginQuery,
};
