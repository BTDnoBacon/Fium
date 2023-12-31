import { Login } from '@/components/organisms';
import { convertClassName, convertClassNameList } from '@/utils';
import styles from './LoginPage.module.scss';
import { Image } from '@/components/atoms';
import { useQuery } from '@tanstack/react-query';
import { Auction } from '@/types';
import { getAuctionsQuery } from '@/api/queries';
import { Swiper } from '@/components/molecules';

interface LoginPageProps {
  className?: string;
  signUp?: boolean;
}

const LoginPage = ({ className, signUp }: LoginPageProps): JSX.Element => {
  const { data: auctions } = useQuery<Auction[], Error>(getAuctionsQuery());

  return (
    <div
      className={convertClassNameList(
        convertClassName(className, styles),
        styles['login-page'],
      )}
    >
      <Swiper type="autoplay">
        {auctions?.map((auction) => {
          return (
            <div
              className={styles['login-page_image-container']}
              key={auction.auctionNo + auction.title}
            >
              <div className={styles.imageWrapper}>
                <Image
                  className={convertClassNameList(
                    convertClassName(className, styles),
                    styles['login-page__image'],
                  )}
                  src={auction?.itemImagePath}
                  alt="aa"
                />
              </div>
            </div>
          );
        })}
      </Swiper>
      {/* <Image
        className={convertClassNameList(styles['login-page__image'])}
        src={
          auctions ? auctions?.[0]?.itemImagePath : '/img/loading/auction.gif'
        }
        alt="image"
      /> */}
      <Login
        className={convertClassNameList(styles['login-page__content'])}
        signUp={signUp}
      />
    </div>
  );
};

export default LoginPage;
