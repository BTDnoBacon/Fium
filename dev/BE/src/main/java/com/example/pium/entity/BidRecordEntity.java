package com.example.pium.entity;


import com.sun.istack.NotNull;
import lombok.*;
import org.hibernate.annotations.DynamicInsert;

import javax.persistence.*;
import java.math.BigInteger;

@AllArgsConstructor
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Data
@Entity
@Builder
@DynamicInsert
@Table(name = "bid_record")
public class BidRecordEntity {

    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    @Column(name = "bid_no")
    private Integer bidNo;

    @NotNull
    @Column(name = "user_no")
    private Integer userNo;

    @NotNull
    @Column(name = "auction_no")
    private Integer auctionNo;

    @NotNull
    @Column(name = "bid_price")
    private Integer bidPrice;

    @NotNull
    @Column(name = "bid_time")
    private BigInteger bidTime;
}
