# Generated from stellaParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .stellaParser import stellaParser
else:
    from stellaParser import stellaParser

# This class defines a complete generic visitor for a parse tree produced by stellaParser.

class stellaParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by stellaParser#start_Program.
    def visitStart_Program(self, ctx:stellaParser.Start_ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#start_Expr.
    def visitStart_Expr(self, ctx:stellaParser.Start_ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#start_Type.
    def visitStart_Type(self, ctx:stellaParser.Start_TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#program.
    def visitProgram(self, ctx:stellaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#LanguageCore.
    def visitLanguageCore(self, ctx:stellaParser.LanguageCoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#AnExtension.
    def visitAnExtension(self, ctx:stellaParser.AnExtensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#DeclFun.
    def visitDeclFun(self, ctx:stellaParser.DeclFunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#DeclFunGeneric.
    def visitDeclFunGeneric(self, ctx:stellaParser.DeclFunGenericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#DeclTypeAlias.
    def visitDeclTypeAlias(self, ctx:stellaParser.DeclTypeAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#DeclExceptionType.
    def visitDeclExceptionType(self, ctx:stellaParser.DeclExceptionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#DeclExceptionVariant.
    def visitDeclExceptionVariant(self, ctx:stellaParser.DeclExceptionVariantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#InlineAnnotation.
    def visitInlineAnnotation(self, ctx:stellaParser.InlineAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#paramDecl.
    def visitParamDecl(self, ctx:stellaParser.ParamDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Fold.
    def visitFold(self, ctx:stellaParser.FoldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Add.
    def visitAdd(self, ctx:stellaParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#IsZero.
    def visitIsZero(self, ctx:stellaParser.IsZeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Var.
    def visitVar(self, ctx:stellaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeAbstraction.
    def visitTypeAbstraction(self, ctx:stellaParser.TypeAbstractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Divide.
    def visitDivide(self, ctx:stellaParser.DivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#LessThan.
    def visitLessThan(self, ctx:stellaParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#DotRecord.
    def visitDotRecord(self, ctx:stellaParser.DotRecordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#GreaterThan.
    def visitGreaterThan(self, ctx:stellaParser.GreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Equal.
    def visitEqual(self, ctx:stellaParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Throw.
    def visitThrow(self, ctx:stellaParser.ThrowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Multiply.
    def visitMultiply(self, ctx:stellaParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#ConstMemory.
    def visitConstMemory(self, ctx:stellaParser.ConstMemoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#List.
    def visitList(self, ctx:stellaParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TryCatch.
    def visitTryCatch(self, ctx:stellaParser.TryCatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Head.
    def visitHead(self, ctx:stellaParser.HeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#NotEqual.
    def visitNotEqual(self, ctx:stellaParser.NotEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#ConstUnit.
    def visitConstUnit(self, ctx:stellaParser.ConstUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Sequence.
    def visitSequence(self, ctx:stellaParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#ConstFalse.
    def visitConstFalse(self, ctx:stellaParser.ConstFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Abstraction.
    def visitAbstraction(self, ctx:stellaParser.AbstractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#ConstInt.
    def visitConstInt(self, ctx:stellaParser.ConstIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Variant.
    def visitVariant(self, ctx:stellaParser.VariantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#ConstTrue.
    def visitConstTrue(self, ctx:stellaParser.ConstTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Subtract.
    def visitSubtract(self, ctx:stellaParser.SubtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeCast.
    def visitTypeCast(self, ctx:stellaParser.TypeCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#If.
    def visitIf(self, ctx:stellaParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Application.
    def visitApplication(self, ctx:stellaParser.ApplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Deref.
    def visitDeref(self, ctx:stellaParser.DerefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#IsEmpty.
    def visitIsEmpty(self, ctx:stellaParser.IsEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Panic.
    def visitPanic(self, ctx:stellaParser.PanicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#LessThanOrEqual.
    def visitLessThanOrEqual(self, ctx:stellaParser.LessThanOrEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Succ.
    def visitSucc(self, ctx:stellaParser.SuccContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Inl.
    def visitInl(self, ctx:stellaParser.InlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#GreaterThanOrEqual.
    def visitGreaterThanOrEqual(self, ctx:stellaParser.GreaterThanOrEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Inr.
    def visitInr(self, ctx:stellaParser.InrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Match.
    def visitMatch(self, ctx:stellaParser.MatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#LogicNot.
    def visitLogicNot(self, ctx:stellaParser.LogicNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#ParenthesisedExpr.
    def visitParenthesisedExpr(self, ctx:stellaParser.ParenthesisedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Tail.
    def visitTail(self, ctx:stellaParser.TailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Record.
    def visitRecord(self, ctx:stellaParser.RecordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#LogicAnd.
    def visitLogicAnd(self, ctx:stellaParser.LogicAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeApplication.
    def visitTypeApplication(self, ctx:stellaParser.TypeApplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#LetRec.
    def visitLetRec(self, ctx:stellaParser.LetRecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#LogicOr.
    def visitLogicOr(self, ctx:stellaParser.LogicOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TryWith.
    def visitTryWith(self, ctx:stellaParser.TryWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Pred.
    def visitPred(self, ctx:stellaParser.PredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeAsc.
    def visitTypeAsc(self, ctx:stellaParser.TypeAscContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#NatRec.
    def visitNatRec(self, ctx:stellaParser.NatRecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Unfold.
    def visitUnfold(self, ctx:stellaParser.UnfoldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Ref.
    def visitRef(self, ctx:stellaParser.RefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#DotTuple.
    def visitDotTuple(self, ctx:stellaParser.DotTupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Fix.
    def visitFix(self, ctx:stellaParser.FixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Let.
    def visitLet(self, ctx:stellaParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Assign.
    def visitAssign(self, ctx:stellaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#Tuple.
    def visitTuple(self, ctx:stellaParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#ConsList.
    def visitConsList(self, ctx:stellaParser.ConsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#patternBinding.
    def visitPatternBinding(self, ctx:stellaParser.PatternBindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#binding.
    def visitBinding(self, ctx:stellaParser.BindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#matchCase.
    def visitMatchCase(self, ctx:stellaParser.MatchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternVariant.
    def visitPatternVariant(self, ctx:stellaParser.PatternVariantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternInl.
    def visitPatternInl(self, ctx:stellaParser.PatternInlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternInr.
    def visitPatternInr(self, ctx:stellaParser.PatternInrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternTuple.
    def visitPatternTuple(self, ctx:stellaParser.PatternTupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternRecord.
    def visitPatternRecord(self, ctx:stellaParser.PatternRecordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternList.
    def visitPatternList(self, ctx:stellaParser.PatternListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternCons.
    def visitPatternCons(self, ctx:stellaParser.PatternConsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternFalse.
    def visitPatternFalse(self, ctx:stellaParser.PatternFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternTrue.
    def visitPatternTrue(self, ctx:stellaParser.PatternTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternUnit.
    def visitPatternUnit(self, ctx:stellaParser.PatternUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternInt.
    def visitPatternInt(self, ctx:stellaParser.PatternIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternSucc.
    def visitPatternSucc(self, ctx:stellaParser.PatternSuccContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#PatternVar.
    def visitPatternVar(self, ctx:stellaParser.PatternVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#ParenthesisedPattern.
    def visitParenthesisedPattern(self, ctx:stellaParser.ParenthesisedPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#labelledPattern.
    def visitLabelledPattern(self, ctx:stellaParser.LabelledPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeTuple.
    def visitTypeTuple(self, ctx:stellaParser.TypeTupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeTop.
    def visitTypeTop(self, ctx:stellaParser.TypeTopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeBool.
    def visitTypeBool(self, ctx:stellaParser.TypeBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeRef.
    def visitTypeRef(self, ctx:stellaParser.TypeRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeRec.
    def visitTypeRec(self, ctx:stellaParser.TypeRecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeSum.
    def visitTypeSum(self, ctx:stellaParser.TypeSumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeVar.
    def visitTypeVar(self, ctx:stellaParser.TypeVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeVariant.
    def visitTypeVariant(self, ctx:stellaParser.TypeVariantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeUnit.
    def visitTypeUnit(self, ctx:stellaParser.TypeUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeNat.
    def visitTypeNat(self, ctx:stellaParser.TypeNatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeBottom.
    def visitTypeBottom(self, ctx:stellaParser.TypeBottomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeParens.
    def visitTypeParens(self, ctx:stellaParser.TypeParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeFun.
    def visitTypeFun(self, ctx:stellaParser.TypeFunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeForAll.
    def visitTypeForAll(self, ctx:stellaParser.TypeForAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeRecord.
    def visitTypeRecord(self, ctx:stellaParser.TypeRecordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#TypeList.
    def visitTypeList(self, ctx:stellaParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#recordFieldType.
    def visitRecordFieldType(self, ctx:stellaParser.RecordFieldTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stellaParser#variantFieldType.
    def visitVariantFieldType(self, ctx:stellaParser.VariantFieldTypeContext):
        return self.visitChildren(ctx)



del stellaParser