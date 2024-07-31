package androidx.compose.ui.layout;

import androidx.compose.ui.geometry.Rect;
import androidx.compose.ui.layout.Placeable;
import androidx.compose.ui.node.LayoutNodeLayoutDelegate;
import androidx.compose.ui.node.LookaheadCapablePlaceable;
import androidx.compose.ui.unit.DpRect;
import androidx.compose.ui.unit.LayoutDirection;
import java.util.Map;
import kotlin.Metadata;
import kotlin.Unit;
import kotlin.collections.MapsKt;
import kotlin.jvm.functions.Function1;
import kotlin.jvm.internal.Intrinsics;

/* compiled from: MeasureScope.kt */
@Metadata(d1 = {"\u00004\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\b\n\u0002\b\u0002\n\u0002\u0010$\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0010\u0002\n\u0002\u0018\u0002\n\u0000\bf\u0018\u00002\u00020\u0001JG\u0010\u0002\u001a\u00020\u00032\u0006\u0010\u0004\u001a\u00020\u00052\u0006\u0010\u0006\u001a\u00020\u00052\u0014\b\u0002\u0010\u0007\u001a\u000e\u0012\u0004\u0012\u00020\t\u0012\u0004\u0012\u00020\u00050\b2\u0017\u0010\n\u001a\u0013\u0012\u0004\u0012\u00020\f\u0012\u0004\u0012\u00020\r0\u000b¢\u0006\u0002\b\u000eH\u0016ø\u0001\u0000\u0082\u0002\u0006\n\u0004\b!0\u0001¨\u0006\u000fÀ\u0006\u0003"}, d2 = {"Landroidx/compose/ui/layout/MeasureScope;", "Landroidx/compose/ui/layout/IntrinsicMeasureScope;", "layout", "Landroidx/compose/ui/layout/MeasureResult;", "width", "", "height", "alignmentLines", "", "Landroidx/compose/ui/layout/AlignmentLine;", "placementBlock", "Lkotlin/Function1;", "Landroidx/compose/ui/layout/Placeable$PlacementScope;", "", "Lkotlin/ExtensionFunctionType;", "ui_release"}, k = 1, mv = {1, 8, 0}, xi = 48)
/* loaded from: classes.dex */
public interface MeasureScope extends IntrinsicMeasureScope {

    /* compiled from: MeasureScope.kt */
    @Metadata(k = 3, mv = {1, 8, 0}, xi = 48)
    /* loaded from: classes.dex */
    public static final class DefaultImpls {
        @Deprecated
        public static boolean isLookingAhead(MeasureScope measureScope) {
            return MeasureScope.super.isLookingAhead();
        }

        @Deprecated
        /* renamed from: roundToPx--R2X_6o */
        public static int m3903roundToPxR2X_6o(MeasureScope measureScope, long j) {
            return MeasureScope.super.mo318roundToPxR2X_6o(j);
        }

        @Deprecated
        /* renamed from: roundToPx-0680j_4 */
        public static int m3904roundToPx0680j_4(MeasureScope measureScope, float f) {
            return MeasureScope.super.mo319roundToPx0680j_4(f);
        }

        @Deprecated
        /* renamed from: toDp-GaN1DYA */
        public static float m3905toDpGaN1DYA(MeasureScope measureScope, long j) {
            return MeasureScope.super.mo320toDpGaN1DYA(j);
        }

        @Deprecated
        /* renamed from: toDp-u2uoSUM */
        public static float m3906toDpu2uoSUM(MeasureScope measureScope, float f) {
            return MeasureScope.super.mo321toDpu2uoSUM(f);
        }

        @Deprecated
        /* renamed from: toDp-u2uoSUM */
        public static float m3907toDpu2uoSUM(MeasureScope measureScope, int i) {
            return MeasureScope.super.mo322toDpu2uoSUM(i);
        }

        @Deprecated
        /* renamed from: toDpSize-k-rfVVM */
        public static long m3908toDpSizekrfVVM(MeasureScope measureScope, long j) {
            return MeasureScope.super.mo323toDpSizekrfVVM(j);
        }

        @Deprecated
        /* renamed from: toPx--R2X_6o */
        public static float m3909toPxR2X_6o(MeasureScope measureScope, long j) {
            return MeasureScope.super.mo324toPxR2X_6o(j);
        }

        @Deprecated
        /* renamed from: toPx-0680j_4 */
        public static float m3910toPx0680j_4(MeasureScope measureScope, float f) {
            return MeasureScope.super.mo325toPx0680j_4(f);
        }

        @Deprecated
        public static Rect toRect(MeasureScope measureScope, DpRect receiver) {
            Intrinsics.checkNotNullParameter(receiver, "$receiver");
            return MeasureScope.super.toRect(receiver);
        }

        @Deprecated
        /* renamed from: toSize-XkaWNTQ */
        public static long m3911toSizeXkaWNTQ(MeasureScope measureScope, long j) {
            return MeasureScope.super.mo326toSizeXkaWNTQ(j);
        }

        @Deprecated
        /* renamed from: toSp-0xMU5do */
        public static long m3912toSp0xMU5do(MeasureScope measureScope, float f) {
            return MeasureScope.super.mo327toSp0xMU5do(f);
        }

        @Deprecated
        /* renamed from: toSp-kPz2Gy4 */
        public static long m3913toSpkPz2Gy4(MeasureScope measureScope, float f) {
            return MeasureScope.super.mo328toSpkPz2Gy4(f);
        }

        @Deprecated
        /* renamed from: toSp-kPz2Gy4 */
        public static long m3914toSpkPz2Gy4(MeasureScope measureScope, int i) {
            return MeasureScope.super.mo329toSpkPz2Gy4(i);
        }

        @Deprecated
        public static MeasureResult layout(MeasureScope measureScope, int i, int i2, Map<AlignmentLine, Integer> alignmentLines, Function1<? super Placeable.PlacementScope, Unit> placementBlock) {
            Intrinsics.checkNotNullParameter(alignmentLines, "alignmentLines");
            Intrinsics.checkNotNullParameter(placementBlock, "placementBlock");
            return MeasureScope.super.layout(i, i2, alignmentLines, placementBlock);
        }
    }

    /* JADX WARN: Multi-variable type inference failed */
    static /* synthetic */ MeasureResult layout$default(MeasureScope measureScope, int i, int i2, Map map, Function1 function1, int i3, Object obj) {
        if (obj != null) {
            throw new UnsupportedOperationException("Super calls with default arguments not supported in this target, function: layout");
        }
        if ((i3 & 4) != 0) {
            map = MapsKt.emptyMap();
        }
        return measureScope.layout(i, i2, map, function1);
    }

    default MeasureResult layout(int width, int height, Map<AlignmentLine, Integer> alignmentLines, Function1<? super Placeable.PlacementScope, Unit> placementBlock) {
        Intrinsics.checkNotNullParameter(alignmentLines, "alignmentLines");
        Intrinsics.checkNotNullParameter(placementBlock, "placementBlock");
        return new MeasureResult(width, height, alignmentLines, this, placementBlock) { // from class: androidx.compose.ui.layout.MeasureScope$layout$1
            final /* synthetic */ Function1<Placeable.PlacementScope, Unit> $placementBlock;
            final /* synthetic */ int $width;
            private final Map<AlignmentLine, Integer> alignmentLines;
            private final int height;
            final /* synthetic */ MeasureScope this$0;
            private final int width;

            @Override // androidx.compose.ui.layout.MeasureResult
            public Map<AlignmentLine, Integer> getAlignmentLines() {
                return this.alignmentLines;
            }

            @Override // androidx.compose.ui.layout.MeasureResult
            public int getHeight() {
                return this.height;
            }

            @Override // androidx.compose.ui.layout.MeasureResult
            public int getWidth() {
                return this.width;
            }

            /* JADX INFO: Access modifiers changed from: package-private */
            /* JADX WARN: Multi-variable type inference failed */
            {
                this.$width = width;
                this.this$0 = this;
                this.$placementBlock = placementBlock;
                this.width = width;
                this.height = height;
                this.alignmentLines = alignmentLines;
            }

            @Override // androidx.compose.ui.layout.MeasureResult
            public void placeChildren() {
                Placeable.PlacementScope.Companion companion = Placeable.PlacementScope.INSTANCE;
                int i = this.$width;
                LayoutDirection layoutDirection = this.this$0.getLayoutDirection();
                MeasureScope measureScope = this.this$0;
                LookaheadCapablePlaceable lookaheadCapablePlaceable = measureScope instanceof LookaheadCapablePlaceable ? (LookaheadCapablePlaceable) measureScope : null;
                Function1<Placeable.PlacementScope, Unit> function1 = this.$placementBlock;
                LayoutCoordinates layoutCoordinates = Placeable.PlacementScope._coordinates;
                int parentWidth = Placeable.PlacementScope.INSTANCE.getParentWidth();
                LayoutDirection parentLayoutDirection = Placeable.PlacementScope.INSTANCE.getParentLayoutDirection();
                LayoutNodeLayoutDelegate layoutNodeLayoutDelegate = Placeable.PlacementScope.layoutDelegate;
                Placeable.PlacementScope.Companion companion2 = Placeable.PlacementScope.INSTANCE;
                Placeable.PlacementScope.parentWidth = i;
                Placeable.PlacementScope.Companion companion3 = Placeable.PlacementScope.INSTANCE;
                Placeable.PlacementScope.parentLayoutDirection = layoutDirection;
                boolean configureForPlacingForAlignment = companion.configureForPlacingForAlignment(lookaheadCapablePlaceable);
                function1.invoke(companion);
                if (lookaheadCapablePlaceable != null) {
                    lookaheadCapablePlaceable.setPlacingForAlignment$ui_release(configureForPlacingForAlignment);
                }
                Placeable.PlacementScope.Companion companion4 = Placeable.PlacementScope.INSTANCE;
                Placeable.PlacementScope.parentWidth = parentWidth;
                Placeable.PlacementScope.Companion companion5 = Placeable.PlacementScope.INSTANCE;
                Placeable.PlacementScope.parentLayoutDirection = parentLayoutDirection;
                Placeable.PlacementScope._coordinates = layoutCoordinates;
                Placeable.PlacementScope.layoutDelegate = layoutNodeLayoutDelegate;
            }
        };
    }
}
