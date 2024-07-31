package androidx.compose.foundation.layout;

import androidx.compose.ui.Modifier;
import androidx.compose.ui.layout.IntrinsicMeasurable;
import androidx.compose.ui.layout.IntrinsicMeasureScope;
import androidx.compose.ui.layout.Measurable;
import androidx.compose.ui.layout.MeasureResult;
import androidx.compose.ui.layout.MeasureScope;
import androidx.compose.ui.layout.Placeable;
import androidx.compose.ui.node.LayoutModifierNode;
import androidx.compose.ui.unit.Constraints;
import androidx.compose.ui.unit.ConstraintsKt;
import androidx.compose.ui.unit.IntSize;
import androidx.compose.ui.unit.IntSizeKt;
import kotlin.Metadata;
import kotlin.Unit;
import kotlin.jvm.functions.Function1;
import kotlin.jvm.internal.Intrinsics;
import kotlin.math.MathKt;

/* compiled from: AspectRatio.kt */
@Metadata(d1 = {"\u0000J\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u0007\n\u0000\n\u0002\u0010\u000b\n\u0002\b\n\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0010\b\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0010\b\u0002\u0018\u00002\u00020\u00012\u00020\u0002B\u0015\u0012\u0006\u0010\u0003\u001a\u00020\u0004\u0012\u0006\u0010\u0005\u001a\u00020\u0006¢\u0006\u0002\u0010\u0007J\u0019\u0010\u0010\u001a\u00020\u0011*\u00020\u0012H\u0002ø\u0001\u0000ø\u0001\u0001¢\u0006\u0004\b\u0013\u0010\u0014J\u001c\u0010\u0015\u001a\u00020\u0016*\u00020\u00172\u0006\u0010\u0018\u001a\u00020\u00192\u0006\u0010\u001a\u001a\u00020\u0016H\u0016J\u001c\u0010\u001b\u001a\u00020\u0016*\u00020\u00172\u0006\u0010\u0018\u001a\u00020\u00192\u0006\u0010\u001c\u001a\u00020\u0016H\u0016J)\u0010\u001d\u001a\u00020\u001e*\u00020\u001f2\u0006\u0010\u0018\u001a\u00020 2\u0006\u0010!\u001a\u00020\u0012H\u0016ø\u0001\u0000ø\u0001\u0001¢\u0006\u0004\b\"\u0010#J\u001c\u0010$\u001a\u00020\u0016*\u00020\u00172\u0006\u0010\u0018\u001a\u00020\u00192\u0006\u0010\u001a\u001a\u00020\u0016H\u0016J\u001c\u0010%\u001a\u00020\u0016*\u00020\u00172\u0006\u0010\u0018\u001a\u00020\u00192\u0006\u0010\u001c\u001a\u00020\u0016H\u0016J#\u0010&\u001a\u00020\u0011*\u00020\u00122\b\b\u0002\u0010'\u001a\u00020\u0006H\u0002ø\u0001\u0000ø\u0001\u0001¢\u0006\u0004\b(\u0010)J#\u0010*\u001a\u00020\u0011*\u00020\u00122\b\b\u0002\u0010'\u001a\u00020\u0006H\u0002ø\u0001\u0000ø\u0001\u0001¢\u0006\u0004\b+\u0010)J#\u0010,\u001a\u00020\u0011*\u00020\u00122\b\b\u0002\u0010'\u001a\u00020\u0006H\u0002ø\u0001\u0000ø\u0001\u0001¢\u0006\u0004\b-\u0010)J#\u0010.\u001a\u00020\u0011*\u00020\u00122\b\b\u0002\u0010'\u001a\u00020\u0006H\u0002ø\u0001\u0000ø\u0001\u0001¢\u0006\u0004\b/\u0010)R\u001a\u0010\u0003\u001a\u00020\u0004X\u0086\u000e¢\u0006\u000e\n\u0000\u001a\u0004\b\b\u0010\t\"\u0004\b\n\u0010\u000bR\u001a\u0010\u0005\u001a\u00020\u0006X\u0086\u000e¢\u0006\u000e\n\u0000\u001a\u0004\b\f\u0010\r\"\u0004\b\u000e\u0010\u000f\u0082\u0002\u000b\n\u0005\b¡\u001e0\u0001\n\u0002\b\u0019¨\u00060"}, d2 = {"Landroidx/compose/foundation/layout/AspectRatioNode;", "Landroidx/compose/ui/node/LayoutModifierNode;", "Landroidx/compose/ui/Modifier$Node;", "aspectRatio", "", "matchHeightConstraintsFirst", "", "(FZ)V", "getAspectRatio", "()F", "setAspectRatio", "(F)V", "getMatchHeightConstraintsFirst", "()Z", "setMatchHeightConstraintsFirst", "(Z)V", "findSize", "Landroidx/compose/ui/unit/IntSize;", "Landroidx/compose/ui/unit/Constraints;", "findSize-ToXhtMw", "(J)J", "maxIntrinsicHeight", "", "Landroidx/compose/ui/layout/IntrinsicMeasureScope;", "measurable", "Landroidx/compose/ui/layout/IntrinsicMeasurable;", "width", "maxIntrinsicWidth", "height", "measure", "Landroidx/compose/ui/layout/MeasureResult;", "Landroidx/compose/ui/layout/MeasureScope;", "Landroidx/compose/ui/layout/Measurable;", "constraints", "measure-3p2s80s", "(Landroidx/compose/ui/layout/MeasureScope;Landroidx/compose/ui/layout/Measurable;J)Landroidx/compose/ui/layout/MeasureResult;", "minIntrinsicHeight", "minIntrinsicWidth", "tryMaxHeight", "enforceConstraints", "tryMaxHeight-JN-0ABg", "(JZ)J", "tryMaxWidth", "tryMaxWidth-JN-0ABg", "tryMinHeight", "tryMinHeight-JN-0ABg", "tryMinWidth", "tryMinWidth-JN-0ABg", "foundation-layout_release"}, k = 1, mv = {1, 8, 0}, xi = 48)
/* loaded from: classes.dex */
final class AspectRatioNode extends Modifier.Node implements LayoutModifierNode {
    private float aspectRatio;
    private boolean matchHeightConstraintsFirst;

    public final float getAspectRatio() {
        return this.aspectRatio;
    }

    public final boolean getMatchHeightConstraintsFirst() {
        return this.matchHeightConstraintsFirst;
    }

    public final void setAspectRatio(float f) {
        this.aspectRatio = f;
    }

    public final void setMatchHeightConstraintsFirst(boolean z) {
        this.matchHeightConstraintsFirst = z;
    }

    public AspectRatioNode(float f, boolean z) {
        this.aspectRatio = f;
        this.matchHeightConstraintsFirst = z;
    }

    @Override // androidx.compose.ui.node.LayoutModifierNode
    /* renamed from: measure-3p2s80s */
    public MeasureResult mo237measure3p2s80s(MeasureScope measure, Measurable measurable, long j) {
        Intrinsics.checkNotNullParameter(measure, "$this$measure");
        Intrinsics.checkNotNullParameter(measurable, "measurable");
        long m408findSizeToXhtMw = m408findSizeToXhtMw(j);
        if (!IntSize.m5031equalsimpl0(m408findSizeToXhtMw, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
            j = Constraints.INSTANCE.m4837fixedJhjzzOo(IntSize.m5033getWidthimpl(m408findSizeToXhtMw), IntSize.m5032getHeightimpl(m408findSizeToXhtMw));
        }
        final Placeable mo3866measureBRTryo0 = measurable.mo3866measureBRTryo0(j);
        return MeasureScope.layout$default(measure, mo3866measureBRTryo0.getWidth(), mo3866measureBRTryo0.getHeight(), null, new Function1<Placeable.PlacementScope, Unit>() { // from class: androidx.compose.foundation.layout.AspectRatioNode$measure$1
            /* JADX INFO: Access modifiers changed from: package-private */
            {
                super(1);
            }

            @Override // kotlin.jvm.functions.Function1
            public /* bridge */ /* synthetic */ Unit invoke(Placeable.PlacementScope placementScope) {
                invoke2(placementScope);
                return Unit.INSTANCE;
            }

            /* renamed from: invoke, reason: avoid collision after fix types in other method */
            public final void invoke2(Placeable.PlacementScope layout) {
                Intrinsics.checkNotNullParameter(layout, "$this$layout");
                Placeable.PlacementScope.placeRelative$default(layout, Placeable.this, 0, 0, 0.0f, 4, null);
            }
        }, 4, null);
    }

    @Override // androidx.compose.ui.node.LayoutModifierNode
    public int minIntrinsicWidth(IntrinsicMeasureScope intrinsicMeasureScope, IntrinsicMeasurable measurable, int i) {
        Intrinsics.checkNotNullParameter(intrinsicMeasureScope, "<this>");
        Intrinsics.checkNotNullParameter(measurable, "measurable");
        if (i != Integer.MAX_VALUE) {
            return MathKt.roundToInt(i * this.aspectRatio);
        }
        return measurable.minIntrinsicWidth(i);
    }

    @Override // androidx.compose.ui.node.LayoutModifierNode
    public int maxIntrinsicWidth(IntrinsicMeasureScope intrinsicMeasureScope, IntrinsicMeasurable measurable, int i) {
        Intrinsics.checkNotNullParameter(intrinsicMeasureScope, "<this>");
        Intrinsics.checkNotNullParameter(measurable, "measurable");
        if (i != Integer.MAX_VALUE) {
            return MathKt.roundToInt(i * this.aspectRatio);
        }
        return measurable.maxIntrinsicWidth(i);
    }

    @Override // androidx.compose.ui.node.LayoutModifierNode
    public int minIntrinsicHeight(IntrinsicMeasureScope intrinsicMeasureScope, IntrinsicMeasurable measurable, int i) {
        Intrinsics.checkNotNullParameter(intrinsicMeasureScope, "<this>");
        Intrinsics.checkNotNullParameter(measurable, "measurable");
        if (i != Integer.MAX_VALUE) {
            return MathKt.roundToInt(i / this.aspectRatio);
        }
        return measurable.minIntrinsicHeight(i);
    }

    @Override // androidx.compose.ui.node.LayoutModifierNode
    public int maxIntrinsicHeight(IntrinsicMeasureScope intrinsicMeasureScope, IntrinsicMeasurable measurable, int i) {
        Intrinsics.checkNotNullParameter(intrinsicMeasureScope, "<this>");
        Intrinsics.checkNotNullParameter(measurable, "measurable");
        if (i != Integer.MAX_VALUE) {
            return MathKt.roundToInt(i / this.aspectRatio);
        }
        return measurable.maxIntrinsicHeight(i);
    }

    /* renamed from: findSize-ToXhtMw, reason: not valid java name */
    private final long m408findSizeToXhtMw(long j) {
        if (!this.matchHeightConstraintsFirst) {
            long m412tryMaxWidthJN0ABg$default = m412tryMaxWidthJN0ABg$default(this, j, false, 1, null);
            if (!IntSize.m5031equalsimpl0(m412tryMaxWidthJN0ABg$default, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m412tryMaxWidthJN0ABg$default;
            }
            long m410tryMaxHeightJN0ABg$default = m410tryMaxHeightJN0ABg$default(this, j, false, 1, null);
            if (!IntSize.m5031equalsimpl0(m410tryMaxHeightJN0ABg$default, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m410tryMaxHeightJN0ABg$default;
            }
            long m416tryMinWidthJN0ABg$default = m416tryMinWidthJN0ABg$default(this, j, false, 1, null);
            if (!IntSize.m5031equalsimpl0(m416tryMinWidthJN0ABg$default, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m416tryMinWidthJN0ABg$default;
            }
            long m414tryMinHeightJN0ABg$default = m414tryMinHeightJN0ABg$default(this, j, false, 1, null);
            if (!IntSize.m5031equalsimpl0(m414tryMinHeightJN0ABg$default, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m414tryMinHeightJN0ABg$default;
            }
            long m411tryMaxWidthJN0ABg = m411tryMaxWidthJN0ABg(j, false);
            if (!IntSize.m5031equalsimpl0(m411tryMaxWidthJN0ABg, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m411tryMaxWidthJN0ABg;
            }
            long m409tryMaxHeightJN0ABg = m409tryMaxHeightJN0ABg(j, false);
            if (!IntSize.m5031equalsimpl0(m409tryMaxHeightJN0ABg, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m409tryMaxHeightJN0ABg;
            }
            long m415tryMinWidthJN0ABg = m415tryMinWidthJN0ABg(j, false);
            if (!IntSize.m5031equalsimpl0(m415tryMinWidthJN0ABg, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m415tryMinWidthJN0ABg;
            }
            long m413tryMinHeightJN0ABg = m413tryMinHeightJN0ABg(j, false);
            if (!IntSize.m5031equalsimpl0(m413tryMinHeightJN0ABg, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m413tryMinHeightJN0ABg;
            }
        } else {
            long m410tryMaxHeightJN0ABg$default2 = m410tryMaxHeightJN0ABg$default(this, j, false, 1, null);
            if (!IntSize.m5031equalsimpl0(m410tryMaxHeightJN0ABg$default2, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m410tryMaxHeightJN0ABg$default2;
            }
            long m412tryMaxWidthJN0ABg$default2 = m412tryMaxWidthJN0ABg$default(this, j, false, 1, null);
            if (!IntSize.m5031equalsimpl0(m412tryMaxWidthJN0ABg$default2, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m412tryMaxWidthJN0ABg$default2;
            }
            long m414tryMinHeightJN0ABg$default2 = m414tryMinHeightJN0ABg$default(this, j, false, 1, null);
            if (!IntSize.m5031equalsimpl0(m414tryMinHeightJN0ABg$default2, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m414tryMinHeightJN0ABg$default2;
            }
            long m416tryMinWidthJN0ABg$default2 = m416tryMinWidthJN0ABg$default(this, j, false, 1, null);
            if (!IntSize.m5031equalsimpl0(m416tryMinWidthJN0ABg$default2, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m416tryMinWidthJN0ABg$default2;
            }
            long m409tryMaxHeightJN0ABg2 = m409tryMaxHeightJN0ABg(j, false);
            if (!IntSize.m5031equalsimpl0(m409tryMaxHeightJN0ABg2, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m409tryMaxHeightJN0ABg2;
            }
            long m411tryMaxWidthJN0ABg2 = m411tryMaxWidthJN0ABg(j, false);
            if (!IntSize.m5031equalsimpl0(m411tryMaxWidthJN0ABg2, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m411tryMaxWidthJN0ABg2;
            }
            long m413tryMinHeightJN0ABg2 = m413tryMinHeightJN0ABg(j, false);
            if (!IntSize.m5031equalsimpl0(m413tryMinHeightJN0ABg2, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m413tryMinHeightJN0ABg2;
            }
            long m415tryMinWidthJN0ABg2 = m415tryMinWidthJN0ABg(j, false);
            if (!IntSize.m5031equalsimpl0(m415tryMinWidthJN0ABg2, IntSize.INSTANCE.m5038getZeroYbymL2g())) {
                return m415tryMinWidthJN0ABg2;
            }
        }
        return IntSize.INSTANCE.m5038getZeroYbymL2g();
    }

    /* renamed from: tryMaxWidth-JN-0ABg$default, reason: not valid java name */
    static /* synthetic */ long m412tryMaxWidthJN0ABg$default(AspectRatioNode aspectRatioNode, long j, boolean z, int i, Object obj) {
        if ((i & 1) != 0) {
            z = true;
        }
        return aspectRatioNode.m411tryMaxWidthJN0ABg(j, z);
    }

    /* renamed from: tryMaxWidth-JN-0ABg, reason: not valid java name */
    private final long m411tryMaxWidthJN0ABg(long j, boolean z) {
        int roundToInt;
        int m4829getMaxWidthimpl = Constraints.m4829getMaxWidthimpl(j);
        if (m4829getMaxWidthimpl != Integer.MAX_VALUE && (roundToInt = MathKt.roundToInt(m4829getMaxWidthimpl / this.aspectRatio)) > 0) {
            long IntSize = IntSizeKt.IntSize(m4829getMaxWidthimpl, roundToInt);
            if (!z || ConstraintsKt.m4844isSatisfiedBy4WqzIAM(j, IntSize)) {
                return IntSize;
            }
        }
        return IntSize.INSTANCE.m5038getZeroYbymL2g();
    }

    /* renamed from: tryMaxHeight-JN-0ABg$default, reason: not valid java name */
    static /* synthetic */ long m410tryMaxHeightJN0ABg$default(AspectRatioNode aspectRatioNode, long j, boolean z, int i, Object obj) {
        if ((i & 1) != 0) {
            z = true;
        }
        return aspectRatioNode.m409tryMaxHeightJN0ABg(j, z);
    }

    /* renamed from: tryMaxHeight-JN-0ABg, reason: not valid java name */
    private final long m409tryMaxHeightJN0ABg(long j, boolean z) {
        int roundToInt;
        int m4828getMaxHeightimpl = Constraints.m4828getMaxHeightimpl(j);
        if (m4828getMaxHeightimpl != Integer.MAX_VALUE && (roundToInt = MathKt.roundToInt(m4828getMaxHeightimpl * this.aspectRatio)) > 0) {
            long IntSize = IntSizeKt.IntSize(roundToInt, m4828getMaxHeightimpl);
            if (!z || ConstraintsKt.m4844isSatisfiedBy4WqzIAM(j, IntSize)) {
                return IntSize;
            }
        }
        return IntSize.INSTANCE.m5038getZeroYbymL2g();
    }

    /* renamed from: tryMinWidth-JN-0ABg$default, reason: not valid java name */
    static /* synthetic */ long m416tryMinWidthJN0ABg$default(AspectRatioNode aspectRatioNode, long j, boolean z, int i, Object obj) {
        if ((i & 1) != 0) {
            z = true;
        }
        return aspectRatioNode.m415tryMinWidthJN0ABg(j, z);
    }

    /* renamed from: tryMinWidth-JN-0ABg, reason: not valid java name */
    private final long m415tryMinWidthJN0ABg(long j, boolean z) {
        int m4831getMinWidthimpl = Constraints.m4831getMinWidthimpl(j);
        int roundToInt = MathKt.roundToInt(m4831getMinWidthimpl / this.aspectRatio);
        if (roundToInt > 0) {
            long IntSize = IntSizeKt.IntSize(m4831getMinWidthimpl, roundToInt);
            if (!z || ConstraintsKt.m4844isSatisfiedBy4WqzIAM(j, IntSize)) {
                return IntSize;
            }
        }
        return IntSize.INSTANCE.m5038getZeroYbymL2g();
    }

    /* renamed from: tryMinHeight-JN-0ABg$default, reason: not valid java name */
    static /* synthetic */ long m414tryMinHeightJN0ABg$default(AspectRatioNode aspectRatioNode, long j, boolean z, int i, Object obj) {
        if ((i & 1) != 0) {
            z = true;
        }
        return aspectRatioNode.m413tryMinHeightJN0ABg(j, z);
    }

    /* renamed from: tryMinHeight-JN-0ABg, reason: not valid java name */
    private final long m413tryMinHeightJN0ABg(long j, boolean z) {
        int m4830getMinHeightimpl = Constraints.m4830getMinHeightimpl(j);
        int roundToInt = MathKt.roundToInt(m4830getMinHeightimpl * this.aspectRatio);
        if (roundToInt > 0) {
            long IntSize = IntSizeKt.IntSize(roundToInt, m4830getMinHeightimpl);
            if (!z || ConstraintsKt.m4844isSatisfiedBy4WqzIAM(j, IntSize)) {
                return IntSize;
            }
        }
        return IntSize.INSTANCE.m5038getZeroYbymL2g();
    }
}
