package kotlin;

import kotlin.jvm.JvmInline;
import kotlin.jvm.internal.Intrinsics;
import kotlin.ranges.UIntRange;
import kotlin.ranges.URangesKt;

/* compiled from: UShort.kt */
@Metadata(d1 = {"\u0000j\n\u0002\u0018\u0002\n\u0002\u0010\u000f\n\u0000\n\u0002\u0010\n\n\u0002\b\t\n\u0002\u0010\b\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0002\b\r\n\u0002\u0010\u000b\n\u0002\u0010\u0000\n\u0002\b!\n\u0002\u0018\u0002\n\u0002\b\u000f\n\u0002\u0010\u0005\n\u0002\b\u0003\n\u0002\u0010\u0006\n\u0002\b\u0003\n\u0002\u0010\u0007\n\u0002\b\u0005\n\u0002\u0010\t\n\u0002\b\u0005\n\u0002\u0010\u000e\n\u0002\b\u000e\b\u0087@\u0018\u0000 v2\b\u0012\u0004\u0012\u00020\u00000\u0001:\u0001vB\u0014\b\u0001\u0012\u0006\u0010\u0002\u001a\u00020\u0003ø\u0001\u0000¢\u0006\u0004\b\u0004\u0010\u0005J\u001b\u0010\b\u001a\u00020\u00002\u0006\u0010\t\u001a\u00020\u0000H\u0087\fø\u0001\u0000¢\u0006\u0004\b\n\u0010\u000bJ\u001b\u0010\f\u001a\u00020\r2\u0006\u0010\t\u001a\u00020\u000eH\u0087\nø\u0001\u0000¢\u0006\u0004\b\u000f\u0010\u0010J\u001b\u0010\f\u001a\u00020\r2\u0006\u0010\t\u001a\u00020\u0011H\u0087\nø\u0001\u0000¢\u0006\u0004\b\u0012\u0010\u0013J\u001b\u0010\f\u001a\u00020\r2\u0006\u0010\t\u001a\u00020\u0014H\u0087\nø\u0001\u0000¢\u0006\u0004\b\u0015\u0010\u0016J\u001b\u0010\f\u001a\u00020\r2\u0006\u0010\t\u001a\u00020\u0000H\u0097\nø\u0001\u0000¢\u0006\u0004\b\u0017\u0010\u0018J\u0016\u0010\u0019\u001a\u00020\u0000H\u0087\nø\u0001\u0001ø\u0001\u0000¢\u0006\u0004\b\u001a\u0010\u0005J\u001b\u0010\u001b\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u000eH\u0087\nø\u0001\u0000¢\u0006\u0004\b\u001c\u0010\u0010J\u001b\u0010\u001b\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0011H\u0087\nø\u0001\u0000¢\u0006\u0004\b\u001d\u0010\u0013J\u001b\u0010\u001b\u001a\u00020\u00142\u0006\u0010\t\u001a\u00020\u0014H\u0087\nø\u0001\u0000¢\u0006\u0004\b\u001e\u0010\u001fJ\u001b\u0010\u001b\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0000H\u0087\nø\u0001\u0000¢\u0006\u0004\b \u0010\u0018J\u001a\u0010!\u001a\u00020\"2\b\u0010\t\u001a\u0004\u0018\u00010#HÖ\u0003¢\u0006\u0004\b$\u0010%J\u001b\u0010&\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u000eH\u0087\bø\u0001\u0000¢\u0006\u0004\b'\u0010\u0010J\u001b\u0010&\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0011H\u0087\bø\u0001\u0000¢\u0006\u0004\b(\u0010\u0013J\u001b\u0010&\u001a\u00020\u00142\u0006\u0010\t\u001a\u00020\u0014H\u0087\bø\u0001\u0000¢\u0006\u0004\b)\u0010\u001fJ\u001b\u0010&\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0000H\u0087\bø\u0001\u0000¢\u0006\u0004\b*\u0010\u0018J\u0010\u0010+\u001a\u00020\rHÖ\u0001¢\u0006\u0004\b,\u0010-J\u0016\u0010.\u001a\u00020\u0000H\u0087\nø\u0001\u0001ø\u0001\u0000¢\u0006\u0004\b/\u0010\u0005J\u0016\u00100\u001a\u00020\u0000H\u0087\bø\u0001\u0001ø\u0001\u0000¢\u0006\u0004\b1\u0010\u0005J\u001b\u00102\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u000eH\u0087\nø\u0001\u0000¢\u0006\u0004\b3\u0010\u0010J\u001b\u00102\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0011H\u0087\nø\u0001\u0000¢\u0006\u0004\b4\u0010\u0013J\u001b\u00102\u001a\u00020\u00142\u0006\u0010\t\u001a\u00020\u0014H\u0087\nø\u0001\u0000¢\u0006\u0004\b5\u0010\u001fJ\u001b\u00102\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0000H\u0087\nø\u0001\u0000¢\u0006\u0004\b6\u0010\u0018J\u001b\u00107\u001a\u00020\u000e2\u0006\u0010\t\u001a\u00020\u000eH\u0087\bø\u0001\u0000¢\u0006\u0004\b8\u00109J\u001b\u00107\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0011H\u0087\bø\u0001\u0000¢\u0006\u0004\b:\u0010\u0013J\u001b\u00107\u001a\u00020\u00142\u0006\u0010\t\u001a\u00020\u0014H\u0087\bø\u0001\u0000¢\u0006\u0004\b;\u0010\u001fJ\u001b\u00107\u001a\u00020\u00002\u0006\u0010\t\u001a\u00020\u0000H\u0087\bø\u0001\u0000¢\u0006\u0004\b<\u0010\u000bJ\u001b\u0010=\u001a\u00020\u00002\u0006\u0010\t\u001a\u00020\u0000H\u0087\fø\u0001\u0000¢\u0006\u0004\b>\u0010\u000bJ\u001b\u0010?\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u000eH\u0087\nø\u0001\u0000¢\u0006\u0004\b@\u0010\u0010J\u001b\u0010?\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0011H\u0087\nø\u0001\u0000¢\u0006\u0004\bA\u0010\u0013J\u001b\u0010?\u001a\u00020\u00142\u0006\u0010\t\u001a\u00020\u0014H\u0087\nø\u0001\u0000¢\u0006\u0004\bB\u0010\u001fJ\u001b\u0010?\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0000H\u0087\nø\u0001\u0000¢\u0006\u0004\bC\u0010\u0018J\u001b\u0010D\u001a\u00020E2\u0006\u0010\t\u001a\u00020\u0000H\u0087\nø\u0001\u0000¢\u0006\u0004\bF\u0010GJ\u001b\u0010H\u001a\u00020E2\u0006\u0010\t\u001a\u00020\u0000H\u0087\nø\u0001\u0000¢\u0006\u0004\bI\u0010GJ\u001b\u0010J\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u000eH\u0087\nø\u0001\u0000¢\u0006\u0004\bK\u0010\u0010J\u001b\u0010J\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0011H\u0087\nø\u0001\u0000¢\u0006\u0004\bL\u0010\u0013J\u001b\u0010J\u001a\u00020\u00142\u0006\u0010\t\u001a\u00020\u0014H\u0087\nø\u0001\u0000¢\u0006\u0004\bM\u0010\u001fJ\u001b\u0010J\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0000H\u0087\nø\u0001\u0000¢\u0006\u0004\bN\u0010\u0018J\u001b\u0010O\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u000eH\u0087\nø\u0001\u0000¢\u0006\u0004\bP\u0010\u0010J\u001b\u0010O\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0011H\u0087\nø\u0001\u0000¢\u0006\u0004\bQ\u0010\u0013J\u001b\u0010O\u001a\u00020\u00142\u0006\u0010\t\u001a\u00020\u0014H\u0087\nø\u0001\u0000¢\u0006\u0004\bR\u0010\u001fJ\u001b\u0010O\u001a\u00020\u00112\u0006\u0010\t\u001a\u00020\u0000H\u0087\nø\u0001\u0000¢\u0006\u0004\bS\u0010\u0018J\u0010\u0010T\u001a\u00020UH\u0087\b¢\u0006\u0004\bV\u0010WJ\u0010\u0010X\u001a\u00020YH\u0087\b¢\u0006\u0004\bZ\u0010[J\u0010\u0010\\\u001a\u00020]H\u0087\b¢\u0006\u0004\b^\u0010_J\u0010\u0010`\u001a\u00020\rH\u0087\b¢\u0006\u0004\ba\u0010-J\u0010\u0010b\u001a\u00020cH\u0087\b¢\u0006\u0004\bd\u0010eJ\u0010\u0010f\u001a\u00020\u0003H\u0087\b¢\u0006\u0004\bg\u0010\u0005J\u000f\u0010h\u001a\u00020iH\u0016¢\u0006\u0004\bj\u0010kJ\u0016\u0010l\u001a\u00020\u000eH\u0087\bø\u0001\u0001ø\u0001\u0000¢\u0006\u0004\bm\u0010WJ\u0016\u0010n\u001a\u00020\u0011H\u0087\bø\u0001\u0001ø\u0001\u0000¢\u0006\u0004\bo\u0010-J\u0016\u0010p\u001a\u00020\u0014H\u0087\bø\u0001\u0001ø\u0001\u0000¢\u0006\u0004\bq\u0010eJ\u0016\u0010r\u001a\u00020\u0000H\u0087\bø\u0001\u0001ø\u0001\u0000¢\u0006\u0004\bs\u0010\u0005J\u001b\u0010t\u001a\u00020\u00002\u0006\u0010\t\u001a\u00020\u0000H\u0087\fø\u0001\u0000¢\u0006\u0004\bu\u0010\u000bR\u0016\u0010\u0002\u001a\u00020\u00038\u0000X\u0081\u0004¢\u0006\b\n\u0000\u0012\u0004\b\u0006\u0010\u0007\u0088\u0001\u0002\u0092\u0001\u00020\u0003ø\u0001\u0000\u0082\u0002\b\n\u0002\b\u0019\n\u0002\b!¨\u0006w"}, d2 = {"Lkotlin/UShort;", "", "data", "", "constructor-impl", "(S)S", "getData$annotations", "()V", "and", "other", "and-xj2QHRw", "(SS)S", "compareTo", "", "Lkotlin/UByte;", "compareTo-7apg3OU", "(SB)I", "Lkotlin/UInt;", "compareTo-WZ4Q5Ns", "(SI)I", "Lkotlin/ULong;", "compareTo-VKZWuLQ", "(SJ)I", "compareTo-xj2QHRw", "(SS)I", "dec", "dec-Mh2AYeg", "div", "div-7apg3OU", "div-WZ4Q5Ns", "div-VKZWuLQ", "(SJ)J", "div-xj2QHRw", "equals", "", "", "equals-impl", "(SLjava/lang/Object;)Z", "floorDiv", "floorDiv-7apg3OU", "floorDiv-WZ4Q5Ns", "floorDiv-VKZWuLQ", "floorDiv-xj2QHRw", "hashCode", "hashCode-impl", "(S)I", "inc", "inc-Mh2AYeg", "inv", "inv-Mh2AYeg", "minus", "minus-7apg3OU", "minus-WZ4Q5Ns", "minus-VKZWuLQ", "minus-xj2QHRw", "mod", "mod-7apg3OU", "(SB)B", "mod-WZ4Q5Ns", "mod-VKZWuLQ", "mod-xj2QHRw", "or", "or-xj2QHRw", "plus", "plus-7apg3OU", "plus-WZ4Q5Ns", "plus-VKZWuLQ", "plus-xj2QHRw", "rangeTo", "Lkotlin/ranges/UIntRange;", "rangeTo-xj2QHRw", "(SS)Lkotlin/ranges/UIntRange;", "rangeUntil", "rangeUntil-xj2QHRw", "rem", "rem-7apg3OU", "rem-WZ4Q5Ns", "rem-VKZWuLQ", "rem-xj2QHRw", "times", "times-7apg3OU", "times-WZ4Q5Ns", "times-VKZWuLQ", "times-xj2QHRw", "toByte", "", "toByte-impl", "(S)B", "toDouble", "", "toDouble-impl", "(S)D", "toFloat", "", "toFloat-impl", "(S)F", "toInt", "toInt-impl", "toLong", "", "toLong-impl", "(S)J", "toShort", "toShort-impl", "toString", "", "toString-impl", "(S)Ljava/lang/String;", "toUByte", "toUByte-w2LRezQ", "toUInt", "toUInt-pVg5ArA", "toULong", "toULong-s-VKNKU", "toUShort", "toUShort-Mh2AYeg", "xor", "xor-xj2QHRw", "Companion", "kotlin-stdlib"}, k = 1, mv = {1, 9, 0}, xi = 48)
@JvmInline
/* loaded from: classes.dex */
public final class UShort implements Comparable<UShort> {
    public static final short MAX_VALUE = -1;
    public static final short MIN_VALUE = 0;
    public static final int SIZE_BITS = 16;
    public static final int SIZE_BYTES = 2;
    private final short data;

    /* renamed from: box-impl, reason: not valid java name */
    public static final /* synthetic */ UShort m5436boximpl(short s) {
        return new UShort(s);
    }

    /* renamed from: constructor-impl, reason: not valid java name */
    public static short m5442constructorimpl(short s) {
        return s;
    }

    /* renamed from: equals-impl, reason: not valid java name */
    public static boolean m5448equalsimpl(short s, Object obj) {
        return (obj instanceof UShort) && s == ((UShort) obj).getData();
    }

    /* renamed from: equals-impl0, reason: not valid java name */
    public static final boolean m5449equalsimpl0(short s, short s2) {
        return s == s2;
    }

    public static /* synthetic */ void getData$annotations() {
    }

    /* renamed from: hashCode-impl, reason: not valid java name */
    public static int m5454hashCodeimpl(short s) {
        return Short.hashCode(s);
    }

    /* renamed from: toByte-impl, reason: not valid java name */
    private static final byte m5480toByteimpl(short s) {
        return (byte) s;
    }

    /* renamed from: toDouble-impl, reason: not valid java name */
    private static final double m5481toDoubleimpl(short s) {
        return s & MAX_VALUE;
    }

    /* renamed from: toFloat-impl, reason: not valid java name */
    private static final float m5482toFloatimpl(short s) {
        return s & MAX_VALUE;
    }

    /* renamed from: toInt-impl, reason: not valid java name */
    private static final int m5483toIntimpl(short s) {
        return s & MAX_VALUE;
    }

    /* renamed from: toLong-impl, reason: not valid java name */
    private static final long m5484toLongimpl(short s) {
        return s & 65535;
    }

    /* renamed from: toShort-impl, reason: not valid java name */
    private static final short m5485toShortimpl(short s) {
        return s;
    }

    /* renamed from: toUShort-Mh2AYeg, reason: not valid java name */
    private static final short m5490toUShortMh2AYeg(short s) {
        return s;
    }

    public boolean equals(Object obj) {
        return m5448equalsimpl(this.data, obj);
    }

    public int hashCode() {
        return m5454hashCodeimpl(this.data);
    }

    /* renamed from: unbox-impl, reason: not valid java name and from getter */
    public final /* synthetic */ short getData() {
        return this.data;
    }

    @Override // java.lang.Comparable
    public /* bridge */ /* synthetic */ int compareTo(UShort uShort) {
        return Intrinsics.compare(getData() & MAX_VALUE, uShort.getData() & MAX_VALUE);
    }

    private /* synthetic */ UShort(short s) {
        this.data = s;
    }

    /* renamed from: compareTo-7apg3OU, reason: not valid java name */
    private static final int m5437compareTo7apg3OU(short s, byte b) {
        return Intrinsics.compare(s & MAX_VALUE, b & UByte.MAX_VALUE);
    }

    /* renamed from: compareTo-xj2QHRw, reason: not valid java name */
    private int m5440compareToxj2QHRw(short s) {
        return Intrinsics.compare(getData() & MAX_VALUE, s & MAX_VALUE);
    }

    /* renamed from: compareTo-xj2QHRw, reason: not valid java name */
    private static int m5441compareToxj2QHRw(short s, short s2) {
        return Intrinsics.compare(s & MAX_VALUE, s2 & MAX_VALUE);
    }

    /* renamed from: compareTo-WZ4Q5Ns, reason: not valid java name */
    private static final int m5439compareToWZ4Q5Ns(short s, int i) {
        return UByte$$ExternalSyntheticBackport0.m$2(UInt.m5256constructorimpl(s & MAX_VALUE), i);
    }

    /* renamed from: compareTo-VKZWuLQ, reason: not valid java name */
    private static final int m5438compareToVKZWuLQ(short s, long j) {
        return UByte$$ExternalSyntheticBackport0.m(ULong.m5335constructorimpl(s & 65535), j);
    }

    /* renamed from: plus-7apg3OU, reason: not valid java name */
    private static final int m5466plus7apg3OU(short s, byte b) {
        return UInt.m5256constructorimpl(UInt.m5256constructorimpl(s & MAX_VALUE) + UInt.m5256constructorimpl(b & UByte.MAX_VALUE));
    }

    /* renamed from: plus-xj2QHRw, reason: not valid java name */
    private static final int m5469plusxj2QHRw(short s, short s2) {
        return UInt.m5256constructorimpl(UInt.m5256constructorimpl(s & MAX_VALUE) + UInt.m5256constructorimpl(s2 & MAX_VALUE));
    }

    /* renamed from: plus-WZ4Q5Ns, reason: not valid java name */
    private static final int m5468plusWZ4Q5Ns(short s, int i) {
        return UInt.m5256constructorimpl(UInt.m5256constructorimpl(s & MAX_VALUE) + i);
    }

    /* renamed from: plus-VKZWuLQ, reason: not valid java name */
    private static final long m5467plusVKZWuLQ(short s, long j) {
        return ULong.m5335constructorimpl(ULong.m5335constructorimpl(s & 65535) + j);
    }

    /* renamed from: minus-7apg3OU, reason: not valid java name */
    private static final int m5457minus7apg3OU(short s, byte b) {
        return UInt.m5256constructorimpl(UInt.m5256constructorimpl(s & MAX_VALUE) - UInt.m5256constructorimpl(b & UByte.MAX_VALUE));
    }

    /* renamed from: minus-xj2QHRw, reason: not valid java name */
    private static final int m5460minusxj2QHRw(short s, short s2) {
        return UInt.m5256constructorimpl(UInt.m5256constructorimpl(s & MAX_VALUE) - UInt.m5256constructorimpl(s2 & MAX_VALUE));
    }

    /* renamed from: minus-WZ4Q5Ns, reason: not valid java name */
    private static final int m5459minusWZ4Q5Ns(short s, int i) {
        return UInt.m5256constructorimpl(UInt.m5256constructorimpl(s & MAX_VALUE) - i);
    }

    /* renamed from: minus-VKZWuLQ, reason: not valid java name */
    private static final long m5458minusVKZWuLQ(short s, long j) {
        return ULong.m5335constructorimpl(ULong.m5335constructorimpl(s & 65535) - j);
    }

    /* renamed from: times-7apg3OU, reason: not valid java name */
    private static final int m5476times7apg3OU(short s, byte b) {
        return UInt.m5256constructorimpl(UInt.m5256constructorimpl(s & MAX_VALUE) * UInt.m5256constructorimpl(b & UByte.MAX_VALUE));
    }

    /* renamed from: times-xj2QHRw, reason: not valid java name */
    private static final int m5479timesxj2QHRw(short s, short s2) {
        return UInt.m5256constructorimpl(UInt.m5256constructorimpl(s & MAX_VALUE) * UInt.m5256constructorimpl(s2 & MAX_VALUE));
    }

    /* renamed from: times-WZ4Q5Ns, reason: not valid java name */
    private static final int m5478timesWZ4Q5Ns(short s, int i) {
        return UInt.m5256constructorimpl(UInt.m5256constructorimpl(s & MAX_VALUE) * i);
    }

    /* renamed from: times-VKZWuLQ, reason: not valid java name */
    private static final long m5477timesVKZWuLQ(short s, long j) {
        return ULong.m5335constructorimpl(ULong.m5335constructorimpl(s & 65535) * j);
    }

    /* renamed from: div-7apg3OU, reason: not valid java name */
    private static final int m5444div7apg3OU(short s, byte b) {
        return UByte$$ExternalSyntheticBackport0.m$1(UInt.m5256constructorimpl(s & MAX_VALUE), UInt.m5256constructorimpl(b & UByte.MAX_VALUE));
    }

    /* renamed from: div-xj2QHRw, reason: not valid java name */
    private static final int m5447divxj2QHRw(short s, short s2) {
        return UByte$$ExternalSyntheticBackport0.m$1(UInt.m5256constructorimpl(s & MAX_VALUE), UInt.m5256constructorimpl(s2 & MAX_VALUE));
    }

    /* renamed from: div-WZ4Q5Ns, reason: not valid java name */
    private static final int m5446divWZ4Q5Ns(short s, int i) {
        return UByte$$ExternalSyntheticBackport0.m$1(UInt.m5256constructorimpl(s & MAX_VALUE), i);
    }

    /* renamed from: div-VKZWuLQ, reason: not valid java name */
    private static final long m5445divVKZWuLQ(short s, long j) {
        return UByte$$ExternalSyntheticBackport0.m$1(ULong.m5335constructorimpl(s & 65535), j);
    }

    /* renamed from: rem-7apg3OU, reason: not valid java name */
    private static final int m5472rem7apg3OU(short s, byte b) {
        return UByte$$ExternalSyntheticBackport0.m(UInt.m5256constructorimpl(s & MAX_VALUE), UInt.m5256constructorimpl(b & UByte.MAX_VALUE));
    }

    /* renamed from: rem-xj2QHRw, reason: not valid java name */
    private static final int m5475remxj2QHRw(short s, short s2) {
        return UByte$$ExternalSyntheticBackport0.m(UInt.m5256constructorimpl(s & MAX_VALUE), UInt.m5256constructorimpl(s2 & MAX_VALUE));
    }

    /* renamed from: rem-WZ4Q5Ns, reason: not valid java name */
    private static final int m5474remWZ4Q5Ns(short s, int i) {
        return UByte$$ExternalSyntheticBackport0.m(UInt.m5256constructorimpl(s & MAX_VALUE), i);
    }

    /* renamed from: rem-VKZWuLQ, reason: not valid java name */
    private static final long m5473remVKZWuLQ(short s, long j) {
        return UByte$$ExternalSyntheticBackport0.m5229m(ULong.m5335constructorimpl(s & 65535), j);
    }

    /* renamed from: floorDiv-7apg3OU, reason: not valid java name */
    private static final int m5450floorDiv7apg3OU(short s, byte b) {
        return UByte$$ExternalSyntheticBackport0.m$1(UInt.m5256constructorimpl(s & MAX_VALUE), UInt.m5256constructorimpl(b & UByte.MAX_VALUE));
    }

    /* renamed from: floorDiv-xj2QHRw, reason: not valid java name */
    private static final int m5453floorDivxj2QHRw(short s, short s2) {
        return UByte$$ExternalSyntheticBackport0.m$1(UInt.m5256constructorimpl(s & MAX_VALUE), UInt.m5256constructorimpl(s2 & MAX_VALUE));
    }

    /* renamed from: floorDiv-WZ4Q5Ns, reason: not valid java name */
    private static final int m5452floorDivWZ4Q5Ns(short s, int i) {
        return UByte$$ExternalSyntheticBackport0.m$1(UInt.m5256constructorimpl(s & MAX_VALUE), i);
    }

    /* renamed from: floorDiv-VKZWuLQ, reason: not valid java name */
    private static final long m5451floorDivVKZWuLQ(short s, long j) {
        return UByte$$ExternalSyntheticBackport0.m$1(ULong.m5335constructorimpl(s & 65535), j);
    }

    /* renamed from: mod-7apg3OU, reason: not valid java name */
    private static final byte m5461mod7apg3OU(short s, byte b) {
        return UByte.m5178constructorimpl((byte) UByte$$ExternalSyntheticBackport0.m(UInt.m5256constructorimpl(s & MAX_VALUE), UInt.m5256constructorimpl(b & UByte.MAX_VALUE)));
    }

    /* renamed from: mod-xj2QHRw, reason: not valid java name */
    private static final short m5464modxj2QHRw(short s, short s2) {
        return m5442constructorimpl((short) UByte$$ExternalSyntheticBackport0.m(UInt.m5256constructorimpl(s & MAX_VALUE), UInt.m5256constructorimpl(s2 & MAX_VALUE)));
    }

    /* renamed from: mod-WZ4Q5Ns, reason: not valid java name */
    private static final int m5463modWZ4Q5Ns(short s, int i) {
        return UByte$$ExternalSyntheticBackport0.m(UInt.m5256constructorimpl(s & MAX_VALUE), i);
    }

    /* renamed from: mod-VKZWuLQ, reason: not valid java name */
    private static final long m5462modVKZWuLQ(short s, long j) {
        return UByte$$ExternalSyntheticBackport0.m5229m(ULong.m5335constructorimpl(s & 65535), j);
    }

    /* renamed from: inc-Mh2AYeg, reason: not valid java name */
    private static final short m5455incMh2AYeg(short s) {
        return m5442constructorimpl((short) (s + 1));
    }

    /* renamed from: dec-Mh2AYeg, reason: not valid java name */
    private static final short m5443decMh2AYeg(short s) {
        return m5442constructorimpl((short) (s - 1));
    }

    /* renamed from: rangeTo-xj2QHRw, reason: not valid java name */
    private static final UIntRange m5470rangeToxj2QHRw(short s, short s2) {
        return new UIntRange(UInt.m5256constructorimpl(s & MAX_VALUE), UInt.m5256constructorimpl(s2 & MAX_VALUE), null);
    }

    /* renamed from: rangeUntil-xj2QHRw, reason: not valid java name */
    private static final UIntRange m5471rangeUntilxj2QHRw(short s, short s2) {
        return URangesKt.m6429untilJ1ME1BU(UInt.m5256constructorimpl(s & MAX_VALUE), UInt.m5256constructorimpl(s2 & MAX_VALUE));
    }

    /* renamed from: and-xj2QHRw, reason: not valid java name */
    private static final short m5435andxj2QHRw(short s, short s2) {
        return m5442constructorimpl((short) (s & s2));
    }

    /* renamed from: or-xj2QHRw, reason: not valid java name */
    private static final short m5465orxj2QHRw(short s, short s2) {
        return m5442constructorimpl((short) (s | s2));
    }

    /* renamed from: xor-xj2QHRw, reason: not valid java name */
    private static final short m5491xorxj2QHRw(short s, short s2) {
        return m5442constructorimpl((short) (s ^ s2));
    }

    /* renamed from: inv-Mh2AYeg, reason: not valid java name */
    private static final short m5456invMh2AYeg(short s) {
        return m5442constructorimpl((short) (~s));
    }

    /* renamed from: toUByte-w2LRezQ, reason: not valid java name */
    private static final byte m5487toUBytew2LRezQ(short s) {
        return UByte.m5178constructorimpl((byte) s);
    }

    /* renamed from: toUInt-pVg5ArA, reason: not valid java name */
    private static final int m5488toUIntpVg5ArA(short s) {
        return UInt.m5256constructorimpl(s & MAX_VALUE);
    }

    /* renamed from: toULong-s-VKNKU, reason: not valid java name */
    private static final long m5489toULongsVKNKU(short s) {
        return ULong.m5335constructorimpl(s & 65535);
    }

    /* renamed from: toString-impl, reason: not valid java name */
    public static String m5486toStringimpl(short s) {
        return String.valueOf(s & MAX_VALUE);
    }

    public String toString() {
        return m5486toStringimpl(this.data);
    }
}
